from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import phi
from phi.playground import Playground, serve_playground_app
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
phi.api= os.getenv("PHI_API_KEY")

agent_search=Agent(
    name="web serach agent",
    role="search web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

## finance agent
agent_finance = Agent(
    name="finance agent",
    role="analyze financial data and provide insights",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=[
        "Use tables to display data"
        
    ],
    show_tool_calls=True,
    markdown=True,
)
app=Playground(
    agents=[agent_search, agent_finance]).get_app()

if __name__ == "__main__":
    serve_playground_app("app:app", reload=True)


