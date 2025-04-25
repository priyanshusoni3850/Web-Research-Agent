from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_BROKER = os.getenv("REDIS_BROKER_URL", "redis://redis-server:6379/0")

celery = Celery("web_research_agent", broker=REDIS_BROKER)
celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
