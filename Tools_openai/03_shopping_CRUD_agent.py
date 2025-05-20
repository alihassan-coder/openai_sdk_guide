from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')


try:
    db_client = MongoClient(os.getenv("MONGODB_URI"))
    # The ismaster command is cheap and does not require auth.
    db_client.admin.command('ismaster')
    print("MongoDB connection successful!")
except Exception as e:
    print("MongoDB connection failed:", e)


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the CRUD operations for the shopping list
@function_tool
async def read_items():
    """Read all items from the shopping list."""
    db = db_client["shopping_list_db"]
    collection = db["shopping_list"]
    items = list(collection.find({}))
    return items

@function_tool
async def create_item(item_name, quantity):
    """Create a new item in the shopping list."""
    db = db_client["shopping_list_db"]
    collection = db["shopping_list"]
    item = {"name": item_name, "quantity": quantity, "status": "not bought"}
    collection.insert_one(item)
    return f"Added {quantity} of {item_name} to your shopping list."

@function_tool
async def update_item(item_name, quantity=None, status=None):
    """Update an item in the shopping list."""
    db = db_client["shopping_list_db"]
    collection = db["shopping_list"]
    update_fields = {}
    if quantity is not None:
        update_fields["quantity"] = quantity
    if status is not None:
        update_fields["status"] = status
    collection.update_one({"name": item_name}, {"$set": update_fields})
    return f"Updated {item_name} in your shopping list."

@function_tool
async def delete_item(item_name):
    """Delete an item from the shopping list."""
    db = db_client["shopping_list_db"]
    collection = db["shopping_list"]
    collection.delete_one({"name": item_name})
    return f"Deleted {item_name} from your shopping list."



agent = Agent(
    name="ShopSmart",
    instructions="""
You are ShopSmart, an AI assistant that helps users manage their shopping list.

Your job is to:
1. Understand user requests like "Add 2 bottles of milk", "Mark bread as bought", "What’s on my shopping list?" or "Delete eggs from my list".
2. Convert natural language input into structured data: item name, quantity, and status (bought/not bought).
3. Use your tools to perform CRUD operations:
   - Create: Add new shopping list items
   - Read: Show current or filtered list (e.g., bought/not bought items)
   - Update: Change quantity or mark as bought/unbought
   - Delete: Remove an item from the list
4. Confirm your actions clearly and politely.
5. Ask for missing info if needed (e.g., quantity).

You are smart, friendly, and focused on helping users stay organized.
""",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[
        read_items,
        create_item,
        update_item,
        delete_item,
    ],  
)

# ... your existing code above remains unchanged ...

print("Welcome to ShopSmart! Type 'exit' to quit.\n")

while True:
    query = input("Enter the query: ")
    if query.lower() in ["exit", "quit"]:
        print("ShopSmart: Goodbye! 🛒")
        break

    result = Runner.run_sync(
        agent,
        query,
    )

    print(result.final_output)


