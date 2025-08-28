# Running Agents with OpenAI SDK: A Comprehensive Guide

This guide explains the three main methods to run agents using the `Runner` class in the OpenAI SDK. Each method serves different use cases and scenarios.




## Detailed Methods Guide

### 1. `Runner.run()` - Asynchronous Execution

The most flexible method that runs the agent asynchronously.

```python
async def translate_text():
    result = await runner.run(
        agent=my_agent,
        input="Translate this to Spanish: Hello, how are you?"
    )
    print(f"Translation: {result.output}")
    print(f"Execution time: {result.execution_time}ms")
```

**Key Features:**
- Full async support
- Returns complete result object
- Best for complex workflows
- Supports error handling

### 2. `Runner.run_sync()` - Synchronous Execution

Perfect for simple scripts or when you can't use async/await.

```python
def get_weather():
    try:
        result = runner.run_sync(
            agent=my_agent,
            input="What's the weather in New York?"
        )
        return result.output
    except Exception as e:
        print(f"Error: {e}")
        return None
```

**Key Features:**
- Simple synchronous execution
- No async/await needed
- Good for scripts and simple applications
- Same result object as async version

### 3. `Runner.run_streamed()` - Real-time Streaming

Ideal for chat applications and real-time updates.

```python
async def chat_interface():
    print("Chat started. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        print("Assistant: ", end="", flush=True)
        async for event in runner.run_streamed(
            agent=my_agent,
            input=user_input
        ):
            if event.type == "text":
                print(event.content, end="", flush=True)
        print()  # New line after response
```

**Key Features:**
- Real-time output streaming
- Perfect for chat interfaces
- Progressive response display
- Event-based updates

## Comparison Table

| Method | Type | Best For | Return Type | Error Handling | Performance |
|--------|------|----------|-------------|----------------|-------------|
| `run()` | Async | Complex workflows, web apps | `RunResult` | Full try/catch support | High |
| `run_sync()` | Sync | Simple scripts, CLI tools | `RunResult` | Basic error handling | Medium |
| `run_streamed()` | Async | Chat apps, real-time UI | `RunResultStreaming` | Event-based errors | High (streaming) |

#  Understanding `RunConfig` - Run Configuration Options in OpenAI SDK

`RunConfig` is a class in the OpenAI SDK that lets you control how an agent is run. It provides settings that apply globally to your run, like which model to use, how random the output should be, and tracing settings.
---

##  What is `RunConfig`?

`RunConfig` is a configuration object. You pass it to the `Runner` when running an agent to control various global options.

---

##  Why use `RunConfig`?

* To control the model used by all agents
* To apply consistent settings (e.g., temperature)
* To add safety filters (guardrails)
* To control tracing and logging for debugging

---

##  How to use `RunConfig`

You create a `RunConfig` object and pass it to your runner method:

```python
from openai import RunConfig

config = RunConfig(
    model="gpt-4",
    model_settings={"temperature": 0.5},
    trace_metadata={"user": "ali123"},
)

result = runner.run_sync(agent=my_agent, input="Hello!", config=config)
print(result.output)
```

---

##  When to use `RunConfig`

* When you want to apply global settings to all agents
* When you need to switch models easily
* When debugging with trace logs
* When using guardrails for safety

---

##  Where to use `RunConfig`

Pass it as a parameter to any `runner.run()`, `runner.run_sync()`, or `runner.run_streamed()` method.

```python
await runner.run(agent=my_agent, input="Test", config=my_config)
```

---

##  Configuration Options

### 1. `model`

* **What**: Set a specific model like `gpt-4`
* **Use case**: To ensure all agents use the same LLM

### 2. `model_provider`

* **What**: Choose a provider (e.g., OpenAI, Azure)
* **Use case**: Useful when switching between providers

### 3. `model_settings`

* **What**: Control LLM behavior (e.g., temperature)
* **Use case**: Make the model more creative or more precise

```python
model_settings={"temperature": 0.7, "top_p": 0.95}
```

### 4. `input_guardrails`

* **What**: Validate or clean inputs before they go to the agent
* **Use case**: Filter bad words, enforce length limits

### 5. `output_guardrails`

* **What**: Validate or filter responses before returning
* **Use case**: Hide sensitive or inappropriate content

### 6. `handoff_input_filter`

* **What**: Edit input before sending it to a new agent
* **Use case**: Customize messages in multi-agent workflows

### 7. `tracing_disabled`

* **What**: Disable trace logging
* **Use case**: Useful in production to avoid storing logs

### 8. `trace_include_sensitive_data`

* **What**: Decide if sensitive data should be included in logs
* **Use case**: Enable for debugging, disable for privacy

### 9. `workflow_name`

* **What**: Name of the workflow for tracing
* **Use case**: Helps group related runs

### 10. `trace_id`

* **What**: Unique ID for the current run
* **Use case**: Track a specific run in the system

### 11. `group_id`

* **What**: Group multiple traces under one ID
* **Use case**: Link related tasks together

### 12. `trace_metadata`

* **What**: Extra data like user ID, session info
* **Use case**: Add context to logs and debugging

```python
trace_metadata={"user": "ali123", "session": "abc456"}
```

---

##  Example with All Settings

```python
from openai import RunConfig

config = RunConfig(
    model="gpt-4",
    model_provider="openai",
    model_settings={"temperature": 0.5},
    input_guardrails=[],
    output_guardrails=[],
    handoff_input_filter=None,
    tracing_disabled=False,
    trace_include_sensitive_data=True,
    workflow_name="chat-session",
    trace_id="run-001",
    group_id="group-123",
    trace_metadata={"user": "ali123"}
)

result = runner.run_sync(agent=my_agent, input="Summarize this text", config=config)
```

---

##  Summary Table

| Option              | What it does            | Why it's useful         |
| ------------------- | ----------------------- | ----------------------- |
| `model`             | Set global LLM          | Control output behavior |
| `model_settings`    | Set temperature, top\_p | Control creativity      |
| `input_guardrails`  | Validate input          | Ensure safety           |
| `output_guardrails` | Validate output         | Filter responses        |
| `tracing_disabled`  | Disable logs            | Use in production       |
| `trace_metadata`    | Add user/session info   | Debugging               |

---

Next, we will explore **exceptions**—how to handle errors while running your agent.
