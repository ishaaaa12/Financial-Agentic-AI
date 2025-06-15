##🧠 Financial Agentic AI

This project implements a multi-agent AI system using Phi to deliver real-time financial analysis and web search capabilities powered by Groq's ultra-fast LLaMA-3.3 70B models.

💼 Features
🔍 Web Search Agent: Uses DuckDuckGo to search for the latest news on companies and topics.

📈 Finance Agent: Retrieves stock prices, analyst recommendations, financial fundamentals, and company news using yfinance.

🤖 Multi-Agent System: A unified AI that coordinates between specialized agents to respond to complex financial queries.

🧩 Tool Use & Source Inclusion: Each agent is equipped with domain-specific tools and configured to always include sources and use tables for structured outputs.

🧹 Safe Search: Includes a custom SafeDuckDuckGo wrapper to ensure clean and valid URLs in search results.

🛠️ Tech Stack
Phi — Agent orchestration and tool integration

Groq API — Ultra-low-latency inference with LLaMA 3.3 70B

DuckDuckGo Search — News and web queries

YFinance — Real-time financial data

Python — Core implementation

.env — API key management (using dotenv)

🚀 How It Works
Agents are created with distinct roles:

web_search_agent: Answers web queries with DuckDuckGo and filters out malformed URLs.

finance_agent: Fetches financial data like analyst recommendations, prices, and fundamentals.

multi_ai_agent: A meta-agent that intelligently delegates the query to the appropriate sub-agent(s).
