# OpenAI Agent Tools - Documentation

## What Are Tools in OpenAI Agents?

In the OpenAI SDK, a **tool** is a function or service that an agent can use to help complete a task. Tools allow agents to go beyond their built-in knowledge and perform actions like calling APIs, working with files, running calculations, or searching for information.

Tools help the agent interact with the outside world or your own systems.

---

## Why Are Tools Important?

Tools are important because they make the AI agent:

- More useful in real applications
- Capable of handling tasks it cannot solve by itself
- Able to access live or private data
- Able to call custom logic or external systems

Without tools, the agent only responds with text based on its training. With tools, it can actually **do** things.

---

## How Do Tools Work?

- You define the tools (such as a function or external resource)
- You register them with the agent
- The agent decides whether to use a tool based on your input
- If needed, the agent calls the tool, waits for the result, and continues the conversation

Tools allow the agent to solve problems step-by-step and make better decisions.

---

## Official Tool Types in OpenAI SDK

Here are the tool types officially supported in the OpenAI SDK:

### 1. Function Tool
- Runs a Python function you define
- Used to handle logic, calculations, formatting, or anything custom
- Example use: convert temperature, calculate tax, search a database

### 2. Code Interpreter (a.k.a. Python Tool)
- Allows the agent to run code in a secure Python environment
- Can handle file reading, math, data analysis, charts, and more
- Often used for advanced use cases like CSV parsing or data visualization

### 3. File Search Tool
- Lets the agent search and retrieve files you have uploaded
- Useful when your assistant needs to read from large documents
- Supports chunked file retrieval and semantic search

### 4. Web Search Tool
- Allows the agent to search the internet in real time
- Useful for getting up-to-date information or answering questions about current events
- Requires connection to a web search provider (e.g. Bing)

### 5. Retrieval Tool
- Lets the agent access private or custom knowledge using a vector store
- You define a knowledge base and the agent can search over it
- Used in retrieval-augmented generation (RAG) systems

### 6. Function Calling Tool (via OpenAI API)
- Similar to Function Tool, but allows structured calls using the OpenAI function calling format
- Used to give the model detailed knowledge of input/output structure
- Helps the model decide when and how to call a function correctly

---
## Writing Effective Docstrings in Python

## What is a Docstring?

A **docstring** (short for documentation string) is a special kind of string in Python that is used to document a function, class, or module. It explains what the function or object does, what inputs it expects, and what it returns.

Docstrings help make your code **easier to understand**, maintain, and use — especially when working in teams or when integrating with tools like the OpenAI SDK.

---

## Why Are Docstrings Important?

- Explain the purpose of a function or class
- Describe input parameters and their types
- Show expected output or return values
- Improve code readability
- Help users and tools (like AI agents) use your code correctly

When using tools in AI agents, a well-written docstring helps the model decide when and how to call the function.

---

## Basic Syntax

A docstring is placed inside triple quotes just after the function definition:

```python
def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    
    Parameters:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
```

## Best Practices for Using Tools

- Use simple and clear function names and descriptions
- Only register the tools your agent actually needs
- Keep the number of tools manageable to avoid confusion
- Define parameters with proper names and types
- Test tool behavior with different user inputs

---



## Conclusion

Tools are a key part of building powerful and intelligent agents using the OpenAI SDK. They allow agents to act, solve problems, access real data, and support real workflows.

By using tools, you can connect the reasoning of AI with the capabilities of your systems, making your applications more flexible, useful, and intelligent.

