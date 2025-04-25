import httpx
from datetime import datetime
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger("NewsTool")

class NewsAggregator:
    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self):
        self.api_key = settings.NEWS_API_KEY

    def fetch_news(self, query: str, from_date: str = None, to_date: str = None, max_results: int = 10) -> list:
        logger.info(f"Fetching news for: {query}")
        params = {
            "q": query,
            "apiKey": self.api_key,
            "language": "en",
            "pageSize": max_results,
            "sortBy": "relevancy"
        }

        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        try:
            response = httpx.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            articles = response.json().get("articles", [])
            return [{
                "title": article["title"],
                "url": article["url"],
                "published_at": article["publishedAt"],
                "source": article["source"]["name"],
                "summary": article["description"]
            } for article in articles]
        except Exception as e:
            logger.error(f"News fetch error: {e}")
            return []
