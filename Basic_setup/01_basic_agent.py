from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

query = input("Enter the query: ")

result = Runner.run_sync(
    agent,
    query,
)

print(result.final_output)