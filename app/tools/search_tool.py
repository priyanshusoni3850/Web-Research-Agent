import httpx
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger("SearchTool")

class WebSearchTool:
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self):
        self.api_key = settings.SEARCH_API_KEY
        self.cx = settings.SEARCH_ENGINE_ID

    def search(self, query: str, num_results: int = 10) -> list:
        logger.info(f"Searching for: {query}")
        params = {
            "key": self.api_key,
            "cx": self.cx,
            "q": query,
            "num": min(num_results, 10)
        }

        try:
            response = httpx.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            results = response.json().get("items", [])
            return [{
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
            } for item in results]
        except Exception as e:
            logger.error(f"Search error: {e}")
            return []
