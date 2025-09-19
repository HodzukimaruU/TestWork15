from typing import List
from datetime import datetime, timezone
from bs4 import BeautifulSoup
import httpx
from models.quotes import Quote  # Pydantic модель

BASE_URL = "https://quotes.toscrape.com"

def fetch_quotes() -> List[Quote]:
    quotes_list: List[Quote] = []
    url = BASE_URL

    while url:
        try:
            response = httpx.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Ошибка при запросе {url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select("div.quote")

        for quote_html in quotes:
            text = quote_html.select_one("span.text").get_text(strip=True)
            author = quote_html.select_one("small.author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in quote_html.select("div.tags a.tag")]
            created_at = datetime.now(timezone.utc)

            quotes_list.append(Quote(
                quote=text,
                author=author,
                tags=tags,
                created_at=created_at
            ))

        next_page = soup.select_one("li.next a")
        url = BASE_URL + next_page['href'] if next_page else None

    return quotes_list
