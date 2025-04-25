from app.tools.news_tool import NewsAggregator

def test_news_aggregator():
    news_tool = NewsAggregator()
    articles = news_tool.fetch_news("technology", max_results=3)
    assert isinstance(articles, list)
    assert len(articles) > 0
    assert "title" in articles[0]
