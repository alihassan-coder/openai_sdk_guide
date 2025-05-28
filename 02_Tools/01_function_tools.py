from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
import os
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


@function_tool
async def time_date() -> str:
    print("Fetching current date and time...")
    """
    Returns the current local date and time with timezone information.

    Uses the datetime module to get the current time including timezone awareness
    for improved accuracy.
    
    Returns:
        str: The current date and time returned as a formatted string.
    """
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).astimezone()
    return now.isoformat()

agent = Agent(
    name="Assistant",
    instructions="You are an expert of agentic AI.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[time_date],
)

query = input("Enter the query: ")

result = Runner.run_sync(
    agent,
    query,
)

print(result.final_output)