from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
from phi.model.groq import Groq

import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

class SafeDuckDuckGo(DuckDuckGo):
    def search(self, query):
        results = super().search(query)
        # Filter out invalid URLs
        return [r for r in results if r.get("url") and r["url"].startswith(("http://", "https://"))]

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

##Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)