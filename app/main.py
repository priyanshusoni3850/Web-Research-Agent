from fastapi import FastAPI
from app.agents.router import agent_router
from app.utils.logger import get_logger

logger = get_logger("web-agent")

app = FastAPI(title="Web Research Agent", version="1.0")

app.include_router(agent_router, prefix="/agent")

@app.get("/")
def read_root():
    logger.info("Root endpoint hit.")
    return {"message": "Web Research Agent is running!"}
