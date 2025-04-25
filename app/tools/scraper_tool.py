import httpx
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from app.utils.logger import get_logger

logger = get_logger("ScraperTool")

class WebScraper:
    def __init__(self, use_js: bool = False):
        self.use_js = use_js

    def scrape(self, url: str) -> str:
        try:
            logger.info(f"Scraping URL: {url}")
            if self.use_js:
                return self.scrape_dynamic(url)
            else:
                return self.scrape_static(url)
        except Exception as e:
            logger.error(f"Scraping failed: {e}")
            return ""

    def scrape_static(self, url: str) -> str:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = httpx.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
        return soup.get_text(separator="\n", strip=True)

    def scrape_dynamic(self, url: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, timeout=30000)
            content = page.content()
            browser.close()
            soup = BeautifulSoup(content, "lxml")
            return soup.get_text(separator="\n", strip=True)
