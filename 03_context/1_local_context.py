from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, RunContextWrapper
from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini-compatible client
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step 1: Define a context class
@dataclass
class User:
    user_id: int

# Step 2: Define a function tool
@function_tool
async def get_user_info(ctx: RunContextWrapper[User]) -> str:
    """Fetches user personal information to personalize responses."""
    user_id = ctx.context.user_id

    if user_id == 1:
        return "User name is Ali. He is 19 years old. Agentic AI Engineer. Likes cricket."
    elif user_id == 2:
        return "User name is Usman. He is 30 years old. Doctor. Likes mountains."
    else:
        return "User not found."

# Step 3: Create the agent
agent = Agent(
    name="simple_personal_assistant",
    instructions="You are a helpful personal assistant. Always personalize answers using the get_user_info tool.",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    ),
    tools=[get_user_info]
)

# Step 4: Get user query and context
query = input("Ask something: ")
user_context = User(user_id=2)  # You can change this to 2 or another ID

# Step 5: Run the agent with the context
result = Runner.run_sync(agent, query, context=user_context)

# Step 6: Show the output
print("Response:", result.final_output)

