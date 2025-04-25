from app.tools.scraper_tool import WebScraper

def test_web_scraper_static():
    scraper = WebScraper()
    content = scraper.scrape("https://www.example.com/")
    assert isinstance(content, str)
    assert len(content) > 20
