from worker import celery
from app.core.context import MCPContext
from app.core.mcp_router import MCPRouter
from app.models.schema import ResearchResponse

@celery.task(name="run_research_agent_task")
def run_research_agent_task(query: str, include_news: bool = True, include_analysis: bool = True) -> dict:
    context = MCPContext(user_query=query)
    agent = MCPRouter(context)
    result: ResearchResponse = agent.run(
        include_news=include_news,
        include_analysis=include_analysis
    )
    return result.model_dump()
