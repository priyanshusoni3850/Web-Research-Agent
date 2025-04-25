from pydantic import BaseModel
from typing import List, Optional

class ResearchQuery(BaseModel):
    query: str
    include_news: Optional[bool] = True
    include_analysis: Optional[bool] = True

class WebResult(BaseModel):
    title: str
    link: str
    snippet: str

class NewsArticle(BaseModel):
    title: str
    url: str
    summary: Optional[str]
    source: Optional[str]
    published_at: Optional[str]

class AnalysisResult(BaseModel):
    summary: str
    relevance_score: int
    entities: List[str]

class ResearchResponse(BaseModel):
    query: str
    web_results: List[WebResult]
    news_articles: List[NewsArticle]
    final_summary: str
    key_entities: List[str]
