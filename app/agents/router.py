from fastapi import APIRouter
from app.models.schema import ResearchQuery, ResearchResponse
from app.core.context import MCPContext
from app.core.mcp_router import MCPRouter
from app.background.tasks import run_research_agent_task


agent_router = APIRouter(tags=["Research Agent"])

@agent_router.post("/", response_model=ResearchResponse)
def run_agent(query: ResearchQuery):
    context = MCPContext(user_query=query.query)
    agent = MCPRouter(context)
    result = agent.run(
        include_news=query.include_news,
        include_analysis=query.include_analysis
    )
    return result

@agent_router.post("/background/")
def run_agent_background(query: ResearchQuery):
    task = run_research_agent_task.delay(
        query=query.query,
        include_news=query.include_news,
        include_analysis=query.include_analysis
    )
    return {"task_id": task.id, "status": "Task started"}