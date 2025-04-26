from fastapi import FastAPI
from app.agents.router import agent_router
from app.utils.logger import get_logger
from fastapi.responses import HTMLResponse

logger = get_logger("web-agent")

app = FastAPI(title="Web Research Agent", version="1.0")

app.include_router(agent_router, prefix="/agent")

@app.get("/")
def read_root():
    logger.info("Root endpoint hit.")
    return HTMLResponse(content="""
        <html>
            <head><title>Web Research Agent</title></head>
            <body>
                <h2>✨ Welcome to the Web Research Agent!</h2>
                <p>📌 Use the command below in your <strong>CMD</strong> to test it:</p>
                <pre><code>curl -X POST https://web-research-agent-tlkb.onrender.com/agent/ -H "Content-Type: application/json" -d "{\\"query\\": \\"impact of AI in healthcare industry in 2025\\"}"</code></pre>
                <p>🧠 This will return a detailed research summary in JSON format.</p>
            </body>
        </html>
    """, status_code=200)