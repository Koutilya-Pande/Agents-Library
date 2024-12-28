from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

## agent de recherche
agent_search=Agent(
    name="web serach agent",
    role="search web for information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

## finance agent
agent_finance = Agent(
    name="finance agent",
    role="analyze financial data and provide insights",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=[
        "Use tables to display data",
    
        "Format numbers appropriately"
    ],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    name="Financial Analysis Team",
    
    team=[agent_search, agent_finance],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=[
        "Always include sources",
        "Use tables to display data of analysts recommendations and news",
        
    ],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for Apple", stream=True)