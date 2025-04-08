import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

# define the agent 
agent:Agent = Agent(
    name="Math mentor",
    instructions="You are a helpful math teacher"
)

# Run the agent synchronously using run_sync
result = Runner.run_sync(
    agent, 
    "hi who are you?"
)

print("\nCALLING AGENT\n")
print("Agent response:", result.final_output)