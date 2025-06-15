from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()

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

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)





multi_ai_agent.print_response("Summary Analyst Recommendation and share the latest news about NVDA", stream=False)
