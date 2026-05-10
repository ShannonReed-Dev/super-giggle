Convert one or more TypeScript files from this project's `typescript/` folder into Python equivalents in the `python/` folder.

## Arguments
$ARGUMENTS

The arguments are one or more filenames (space-separated). Each filename may include or omit the `.ts` extension. Examples:
- `001_requests.ts`
- `001_requests`
- `001_requests.ts 002_multi-turn-conversations.ts`

## Steps

For each filename in the arguments:

1. Normalize the filename: ensure it ends with `.ts` if no extension was provided.
2. Read the source file from `typescript/<filename>`.
3. Convert the content to Python following the translation rules below.
4. Write the output to `python/<filename with .py extension>`.
5. Confirm which file was created.

## Translation Rules

Apply these rules when converting TypeScript to Python:

### Imports and setup
- `import Anthropic from "@anthropic-ai/sdk"` → `from anthropic import Anthropic`
- `import * as dotenv from "dotenv"` + `dotenv.config()` → `from dotenv import load_dotenv` + `load_dotenv()`
- Remove `import * as readline from "readline"` (Python uses built-in `input()`)
- Remove all other TypeScript-only imports

### Client and model
- `const client = new Anthropic()` → `client = Anthropic()`
- `const model = "..."` → `model = "..."`

### API calls
- `await client.messages.create(...)` → `client.messages.create(...)`
- Remove `async` and `await` keywords throughout

### Response extraction
- `(message.content[0] as Anthropic.TextBlock).text` → `message.content[0].text`
- `(res.content[0] as Anthropic.TextBlock).text` → `res.content[0].text`

### Message arrays
- `const messages: Anthropic.MessageParam[] = []` → `messages = []`
- `{ role: "user", content: text }` → `{"role": "user", "content": text}`

### Functions
- `const funcName = (messages: Anthropic.MessageParam[], text: string): void =>` → `def funcName(messages, text):`
- `const chat = async (messages: Anthropic.MessageParam[]): Promise<string> =>` → `def chat(messages):`
- `const chat = async (messages: Anthropic.MessageParam[], prompt?: string): Promise<string> =>` → `def chat(messages, prompt=None):`
- `const chat = async (messages: Anthropic.MessageParam[], prompt?: string, temperature: number = 1.0): Promise<string> =>` → `def chat(messages, prompt=None, temperature=1.0):`
- Arrow function bodies with `{}` blocks become indented `def` bodies
- `return (message.content[0] as Anthropic.TextBlock).text` → `return message.content[0].text`

### Params object
- `const params: Anthropic.MessageCreateParamsNonStreaming = { model, max_tokens: 1000, messages }` →
  `params = { "model": model, "max_tokens": 1000, "messages": messages }`
- `params.system = prompt` → `params["system"] = prompt`
- `client.messages.create(params)` → `client.messages.create(**params)`

### User input
Replace the readline pattern with Python's `input()`:
```python
user_input = input("> ")
```
Remove the `rl`, `askQuestion`, and `readline.createInterface` lines entirely.

### Control flow
- `while (true)` → `while True:`
- `else if` → `elif`
- `if (x === undefined)` → `if x is None:`
- `if (prompt)` → `if prompt:`
- Remove `break` only if it was added purely for TypeScript loop mechanics (keep intentional breaks)

### String formatting
- `` `text ${var}` `` → `f"text {var}"`
- `String(result)` → `str(result)`

### Output
- `console.log(x)` → `print(x)`
- `process.stdout.write(chunk)` → `print(chunk, end="", flush=True)`
- `console.log()` (empty newline) → `print()`

### Streaming
- `await client.messages.create({ ..., stream: true })` → `client.messages.create(**{..., "stream": True})`
- `for await (const event of stream)` → `for event in stream:`
- `event.type === "content_block_delta"` → `event.type == "content_block_delta"`
- `event.delta.type === "text_delta"` → `event.delta.type == "text_delta"`
- `const stream = client.messages.stream(...)` → use `with client.messages.stream(...) as stream:`
- `for await (const chunk of stream.textStream)` → `for text in stream.text_stream:`
- `await stream.finalMessage()` → `stream.get_final_message()`

### Tool use (agentic loop)
- `const tools: Anthropic.Tool[] = [{ name: ..., input_schema: ... }]` → `tools = [{ "name": ..., "input_schema": ... }]`
- `const toolBlock = res.content.find((b): b is Anthropic.ToolUseBlock => b.type === "tool_use")!` →
  `tool_block = next(b for b in res.content if b.type == "tool_use")`
- `const input = toolBlock.input as { expression: string }; input.expression` → `tool_block.input["expression"]`
- `toolBlock.id` → `tool_block.id`
- `toolBlock.name` → `tool_block.name`
- `tool_use_id: toolBlock.id` → `"tool_use_id": tool_block.id`
- `res.stop_reason === "end_turn"` → `res.stop_reason == "end_turn"`
- `res.stop_reason === "tool_use"` → `res.stop_reason == "tool_use"`

### Top-level code structure
Remove the `async main()` wrapper and `main()` call at the bottom. All code that was inside `main()` should become top-level code, maintaining its indentation relative to the surrounding structure.

### Type annotations
Remove all TypeScript type annotations:
- `: string`, `: number`, `: boolean`, `: void`
- `: Promise<string>`, `: Anthropic.MessageParam[]`
- `as Anthropic.TextBlock`, `as Anthropic.ToolUseBlock`
- Interface and type declarations

### Preserve everything else
- Keep all comments exactly as written (translate `//` comments to `#` comments)
- Keep the same section headers and learning notes
- Keep the same variable names (converted to snake_case where appropriate: `toolBlock` → `tool_block`, `userInput` → `user_input`, `fullResponse` → `full_response`)
- Keep commented-out code blocks commented out in Python syntax (`#` instead of `//`)
