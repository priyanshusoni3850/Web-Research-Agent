from app.core.context import MCPContext
from app.core.mcp_router import MCPRouter

def test_full_pipeline():
    context = MCPContext("impact of AI on healthcare")
    agent = MCPRouter(context)
    response = agent.run()
    assert response.query == "impact of AI on healthcare"
    assert isinstance(response.web_results, list)
    assert isinstance(response.news_articles, list)
