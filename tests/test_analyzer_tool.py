from app.tools.analyzer_tool import ContentAnalyzer

def test_content_analyzer():
    analyzer = ContentAnalyzer()
    text = "OpenAI is a leading AI research lab located in San Francisco."
    result = analyzer.analyze(text, query="AI research")
    assert isinstance(result, dict)
    assert "summary" in result
    assert "entities" in result
