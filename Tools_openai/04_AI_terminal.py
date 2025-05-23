from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define a terminal execution tool
@function_tool
def run_terminal_command(command: str) -> str:
    """Executes a terminal command and returns its output."""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

# Improved Agent definition
agent = Agent(
    name="Lora Terminal Assistant",
    instructions="""
You are Lora, an AI-powered terminal assistant built on Google's Gemini model. 
You help users navigate and operate the terminal using natural language, perform command executions, explain outputs, and assist with system tasks.
Respond clearly and concisely.
""",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[run_terminal_command],
)

# Input/output
while True:
    query = input("Lora Terminal Assistant > ")
    if query.strip().lower() in {"exit", "quit"}:
        print("Goodbye!")
        break
    result = Runner.run_sync(agent, query)
    print("\n Lora's Response:")
    print(result.final_output)


query = input("Lora Terminal Assistant > ")

result = Runner.run_sync(agent, query)

print("\n Lora's Response:")
print(result.final_output)
