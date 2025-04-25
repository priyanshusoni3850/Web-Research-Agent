class MCPContext:
    def __init__(self, user_query: str):
        self.user_query = user_query
        self.web_results = []
        self.news_articles = []
        self.scraped_texts = []
        self.analysis = []

    def add_web_results(self, results):
        self.web_results.extend(results)

    def add_news_articles(self, articles):
        self.news_articles.extend(articles)

    def add_scraped_text(self, text):
        self.scraped_texts.append(text)

    def add_analysis(self, result):
        self.analysis.append(result)

    def get_combined_text(self) -> str:
        return "\n\n".join(self.scraped_texts)
