from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai.types.responses import ResponseTextDeltaEvent
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)



async def main():
    agent = Agent(
    name="Assistant",
    instructions="You are an AI expert.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )
    query = input("Enter the query:")
    result = Runner.run_streamed(agent, input=query)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


asyncio.run(main())   

