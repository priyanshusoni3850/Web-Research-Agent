from app.tools.search_tool import WebSearchTool

def test_web_search_tool():
    search_tool = WebSearchTool()
    results = search_tool.search("latest AI trends", num_results=3)
    assert isinstance(results, list)
    assert len(results) > 0
    assert "title" in results[0]
    assert "link" in results[0]
