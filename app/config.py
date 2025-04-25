import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE_URL: str = os.getenv("OPENAI_API_BASE_URL")  # 🛠️ ADD THIS
    HUGGINGFACE_API_TOKEN: str = os.getenv("HUGGINGFACE_API_TOKEN")  # 🛠️ ADD THIS
    SEARCH_API_KEY: str = os.getenv("SEARCH_API_KEY")
    SEARCH_ENGINE_ID: str = os.getenv("SEARCH_ENGINE_ID")
    NEWS_API_KEY: str = os.getenv("NEWS_API_KEY")
    ENV: str = os.getenv("ENV", "development")


settings = Settings()
