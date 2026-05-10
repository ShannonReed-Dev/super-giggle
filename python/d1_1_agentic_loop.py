#Load env Variables----------------------------------------------------
from dotenv import load_dotenv
from anthropic import Anthropic

#================================================
# Agentic Loop - Calculator Agent
#================================================

load_dotenv()


# Create Client-------------------------------------------------------
client = Anthropic()
model = "claude-haiku-4-5"


tools = [{
    "name": "calculate",
    "description": "Evaluates a math expression and returns the result",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to evaluate, e.g. '24 * 7'"
            }
        },
        "required": ["expression"]
    }
}]


# The actual Python function that runs when Claude calls the tool
def calculate(expression):
    return eval(expression)


# Initial user message - the question we want the agent to answer
messages = [{"role": "user", "content": "What is 12 x 12?"}]

while True:
    res = client.messages.create(
        model=model,
        messages=messages,
        tools=tools,
        max_tokens=1024
    )

    # Stage 2: Claude is done - print the final answer and exit the loop
    if res.stop_reason == "end_turn":
        print(res.content[0].text)
        break

    # Stage 2 (alternate): Claude wants to use a tool
    elif res.stop_reason == "tool_use":
        # Find the tool_use block in Claude's response
        tool_block = next(b for b in res.content if b.type == "tool_use")

        # Stage 3: Run the tool locally with the inputs Claude provided
        result = calculate(tool_block.input["expression"])
        print(f"Tool called: {tool_block.name}({tool_block.input['expression']}) = {result}")

        # Stage 4: Append Claude's full response, then the tool result
        messages.append({"role": "assistant", "content": res.content})
        messages.append({
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": str(result)
            }]
        })
