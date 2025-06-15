<h1>🧠 Financial Agentic AI</h1>

This project implements a multi-agent AI system using Phi to deliver real-time financial analysis and web search capabilities powered by Groq's ultra-fast LLaMA-3.3 70B models.

<h2>💼 Features</h2>

* 🔍 **Web Search Agent:** Uses DuckDuckGo to search for the latest news on companies and topics.

* 📈 **Finance Agent:** Retrieves stock prices, analyst recommendations, financial fundamentals, and company news using yfinance.

* 🤖 **Multi-Agent System:** A unified AI that coordinates between specialized agents to respond to complex financial queries.

* 🧩 **Tool Use & Source Inclusion:** Each agent is equipped with domain-specific tools and configured to always include sources and use tables for structured outputs.

* 🧹 **Safe Search:** Includes a custom SafeDuckDuckGo wrapper to ensure clean and valid URLs in search results.

<h2>🛠️ Tech Stack</h2>

* Phi — Agent orchestration and tool integration

* Groq API — Ultra-low-latency inference with LLaMA 3.3 70B

* DuckDuckGo Search — News and web queries

* YFinance — Real-time financial data

* Python — Core implementation

* .env — API key management (using dotenv)

<h2>🚀 How It Works</h2>
Agents are created with distinct roles:

* web_search_agent: Answers web queries with DuckDuckGo and filters out malformed URLs.

* finance_agent: Fetches financial data like analyst recommendations, prices, and fundamentals.

* multi_ai_agent: A meta-agent that intelligently delegates the query to the appropriate sub-agent(s).

<h2>🔑 Setup</h2>

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/financial-agentic-ai.git
cd financial-agentic-ai
```

---

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

3. **Create a `.env` file:**

```bash
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
```

---

4. **Run the agent:**

```bash
python financial_agent.py
```
