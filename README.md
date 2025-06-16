<h1>🧠 Financial Agentic AI</h1>

This project implements a multi-agent AI system using Phi to deliver real-time financial analysis and web search capabilities powered by Groq's ultra-fast LLaMA-3.3 70B models.

This assistant can:

🔍 Search the web and provide sources

📊 Fetch financial insights like stock prices, analyst recommendations, fundamentals, and news

💡 Summarize and present results in markdown with tables



<h2>💼 Features</h2>

* **Multi-agent setup:** Separate agents for finance and web search

* **LLM-powered reasoning** using Groq models

* **Live financial data** via Yahoo Finance

* **Web search** using DuckDuckGo

* **Phidata Playground** for a clean UI experience

<h2>🛠️ Tech Stack</h2>

* Phi — Agent orchestration and tool integration

* Groq API — Ultra-low-latency inference with LLaMA 3.3 70B

* DuckDuckGo Search — News and web queries

* YFinance — Real-time financial data

* Python — Core implementation


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

<h2>🧠 How to Use the Playground UI</h2>
⚠️ The app does not launch a UI by default.

To interact with your agent through the Phidata Playground interface:

1. Run the script:

```bash
python financial_agent.py
```

2. Copy the local URL shown (e.g., http://localhost:7777)

3. Go to Phidata website

4. Log in

5. Click on the “Playground” section

6. Paste your local URL in the Endpoint field

Interact with your multi-agent system!

