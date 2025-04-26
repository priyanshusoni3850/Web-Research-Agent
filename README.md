# 🌐 Web Research Agent

A smart AI Agent that **searches**, **scrapes**, **analyzes**, and **summarizes** web content based on user queries.

Get complete research reports with a single API call!

---

## 🚀 Live Demo Link
**Use without installing anything!**

👉 [https://web-research-agent-tlkb.onrender.com](https://web-research-agent-tlkb.onrender.com)

---

## 🧪 How to Test Quickly (No Install)

Copy and paste this in your  CMD ONLY:

```bash
curl -X POST https://web-research-agent-tlkb.onrender.com/agent/ -H "Content-Type: application/json" -d "{\"query\": \"impact of AI in healthcare industry in 2025\"}"

✅ You will receive a full JSON response with web results, news, summary, and key entities!

✏️ How to Change Query
Just change inside "query": "..."

Example for a different topic:

bash
Copy
Edit

curl -X POST https://web-research-agent-tlkb.onrender.com/agent/ -H "Content-Type: application/json" -d "{\"query\": \"future of renewable energy in 2030\"}"

🛠️ Full Project Setup Locally (Copy Paste This)
bash
Copy
Edit
# 1. Clone repository
git clone https://github.com/your-username/web-research-agent.git
cd web-research-agent

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# 4. Download spaCy model
python -m spacy download en_core_web_sm

# 5. Install Playwright dependencies
playwright install

# 6. Create a .env file with:
# (These keys are needed only if running locally)
# Example:
echo "SEARCH_API_KEY=your_key" >> .env
echo "SEARCH_ENGINE_ID=your_id" >> .env
echo "NEWS_API_KEY=your_key" >> .env
echo "HUGGINGFACE_API_TOKEN=your_token" >> .env
echo "ENV=development" >> .env

# 7. Run the project
uvicorn app.main:app --reload
✅ Done! Access at: http://127.0.0.1:8000/docs

🐳 Docker Setup (for Deployment)
bash
Copy
Edit
# Build and run using docker-compose
docker-compose up --build
This launches:

FastAPI app

Redis server

Celery background worker

Access API at: http://localhost:8000/docs

📂 Full Project Directory Structure
arduino
Copy
Edit
web_research_agent/
├── app/
│   ├── agents/
│   │   └── agent_router.py
│   ├── core/
│   │   └── mcp_router.py
│   ├── tools/
│   │   ├── search_tool.py
│   │   ├── news_tool.py
│   │   ├── scraper_tool.py
│   │   └── analyzer_tool.py
│   ├── utils/
│   │   ├── logger.py
│   │   └── helper_functions.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── test_agent.py
│   ├── test_search_tool.py
│   └── test_news_tool.py
├── worker/
│   └── celery.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env
└── .dockerignore
📜 Features
🌍 Google Search API + News scraping

📜 Summarization using HuggingFace model (BART-large-cnn)

🏷️ Entity Extraction (NER) using SpaCy

⚡ Async FastAPI backend

🛠️ Celery background tasks with Redis

🐳 Fully Dockerized project

🌎 Public deployment on Render

❗ Important Notes
jq is optional for beautifying output. Not mandatory.

.env secrets are needed only when running locally, not on Render.

Docker handles multiple services automatically (Redis + Worker + App).

✨ Author
Made with ❤️ by [Your Name]

🛡 License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

# ⚡ Quick Recap

| ✅ | Included |
|:--|:--|
| Full copy-paste installation bash | ✔️ |
| Beautiful Directory Structure | ✔️ |
| How to use live link with curl | ✔️ |
| How to change query easily | ✔️ |
| Full local + docker setup explained | ✔️ |

---

Would you also like me to now prepare a **perfect GitHub `repository description`, `topics` and `tags`** setup so it looks 10x more professional? 🚀  
Shall I continue? 🔥  
(Will take just 1 min extra!)  ✅