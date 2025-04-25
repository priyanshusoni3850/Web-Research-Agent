from app.core.context import MCPContext
from app.tools.search_tool import WebSearchTool
from app.tools.news_tool import NewsAggregator
from app.tools.scraper_tool import WebScraper
from app.tools.analyzer_tool import ContentAnalyzer
from app.utils.logger import get_logger
from app.models.schema import ResearchResponse, WebResult, NewsArticle

logger = get_logger("MCPRouter")

class MCPRouter:
    def __init__(self, context: MCPContext):
        self.context = context
        self.search_tool = WebSearchTool()
        self.news_tool = NewsAggregator()
        self.scraper = WebScraper()
        self.analyzer = ContentAnalyzer()

    def run(self, include_news: bool = True, include_analysis: bool = True) -> ResearchResponse:
        # 1. Web Search
        web_results = self.search_tool.search(self.context.user_query)
        self.context.add_web_results(web_results)

        # 2. News Aggregation
        if include_news:
            news_articles = self.news_tool.fetch_news(self.context.user_query)
            self.context.add_news_articles(news_articles)

        # 3. Content Scraping
        for result in web_results[:5]:
            try:
                text = self.scraper.scrape(result["link"])
                if text:
                    self.context.add_scraped_text(text)
            except Exception as e:
                logger.error(f"Scraping failed for {result['link']}: {str(e)}")

        # 4. Content Analysis
        analysis_result = {
            "summary": "",
            "relevance_score": 0,
            "entities": []
        }

        if include_analysis:
            combined_text = self.context.get_combined_text()

            # PATCH: Only analyze if there is sufficient text
            if combined_text and len(combined_text.strip()) > 100:
                try:
                    analysis_result = self.analyzer.analyze(combined_text, self.context.user_query)
                except Exception as e:
                    logger.error(f"Analysis failed: {str(e)}")
            else:
                logger.warning("Not enough combined text to perform analysis. Skipping summarization.")

        # 5. Build Response
        return ResearchResponse(
            query=self.context.user_query,
            web_results=[WebResult(**r) for r in web_results],
            news_articles=[NewsArticle(**a) for a in self.context.news_articles],
            final_summary=analysis_result["summary"],
            key_entities=analysis_result["entities"]
        )
