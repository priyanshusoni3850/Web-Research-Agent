import spacy
import requests
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger("AnalyzerTool")

class ContentAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, text: str, query: str) -> dict:
        if not text:
            return {"summary": "", "entities": [], "relevance_score": 0}

        logger.info("Analyzing content relevance and summary.")
        summary = self.summarize(text, query)
        entities = self.extract_entities(text)
        relevance = self.score_relevance(text, query)

        return {
            "summary": summary,
            "entities": entities,
            "relevance_score": relevance
        }

    def summarize(self, text: str, query: str) -> str:
        prompt = f"Summarize the following content based on the query: '{query}'. Content: {text[:3000]}"
        try:
            url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {
                "Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"  # You need a free token
            }
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_length": 300,
                    "min_length": 50,
                    "do_sample": False
                }
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()[0]["summary_text"].strip()
        except Exception as e:
            logger.error(f"Summarization failed: {e}")
            return ""

    def extract_entities(self, text: str) -> list:
        doc = self.nlp(text)
        return list(set(ent.text for ent in doc.ents if ent.label_ in ["ORG", "PERSON", "GPE", "DATE"]))

    def score_relevance(self, text: str, query: str) -> int:
        return sum(word.lower() in text.lower() for word in query.split())
