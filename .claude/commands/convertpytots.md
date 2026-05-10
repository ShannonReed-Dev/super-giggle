Convert one or more Python files from this project's `python/` folder into TypeScript equivalents in the `typescript/` folder.

## Arguments
$ARGUMENTS

The arguments are one or more filenames (space-separated). Each filename may include or omit the `.py` extension. Examples:
- `001_requests.py`
- `001_requests`
- `001_requests.py 002_multi-turn-conversations.py`

## Steps

For each filename in the arguments:

1. Normalize the filename: ensure it ends with `.py` if no extension was provided.
2. Read the source file from `python/<filename>`.
3. Convert the content to TypeScript following the translation rules below.
4. Write the output to `typescript/<filename with .ts extension>`.
5. Confirm which file was created.

## Translation Rules

Apply these rules when converting Python to TypeScript:

### Imports and setup
- `from anthropic import Anthropic` → `import Anthropic from "@anthropic-ai/sdk"`
- `from dotenv import load_dotenv` + `load_dotenv()` → `import * as dotenv from "dotenv"` + `dotenv.config()`
- Add `import * as readline from "readline"` if the file uses `input()`

### Client and model
- `client = Anthropic()` → `const client = new Anthropic()`
- `model = "..."` → `const model = "..."`

### API calls
- `client.messages.create(...)` → `await client.messages.create(...)`
- All API calls are async - any function that calls the API must be `async`

### Response extraction
- `message.content[0].text` → `(message.content[0] as Anthropic.TextBlock).text`
- `res.content[0].text` → `(res.content[0] as Anthropic.TextBlock).text`

### Message arrays
- `messages = []` → `const messages: Anthropic.MessageParam[] = []`
- Message dicts `{"role": "user", "content": text}` → `{ role: "user", content: text }`

### Functions
- `def funcName(messages, text):` → `const funcName = (messages: Anthropic.MessageParam[], text: string): void =>`
- `def chat(messages):` → `const chat = async (messages: Anthropic.MessageParam[]): Promise<string> =>`
- `def chat(messages, prompt=None):` → `const chat = async (messages: Anthropic.MessageParam[], prompt?: string): Promise<string> =>`
- `def chat(messages, prompt=None, temperature=1.0):` → `const chat = async (messages: Anthropic.MessageParam[], prompt?: string, temperature: number = 1.0): Promise<string> =>`
- `return message.content[0].text` → `return (message.content[0] as Anthropic.TextBlock).text`

### Params object (for conditional system/temperature)
- `params = { "model": model, ... }` → `const params: Anthropic.MessageCreateParamsNonStreaming = { model, ... }`
- `params["system"] = prompt` → `params.system = prompt`
- `client.messages.create(**params)` → `client.messages.create(params)`

### User input
Replace Python's `input()` pattern with a readline Promise wrapper:
```typescript
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const askQuestion = (prompt: string): Promise<string> =>
    new Promise((resolve) => rl.question(prompt, resolve));
const userInput = await askQuestion("> ");
```

### Control flow
- `while True:` → `while (true)`
- `elif` → `else if`
- `if x is None:` → `if (x === undefined)`
- `if prompt:` → `if (prompt)`

### String formatting
- `f"text {var}"` → `` `text ${var}` ``
- `f"Tool called: {tool_block.name}({tool_block.input['expression']}) = {result}"` → `` `Tool called: ${toolBlock.name}(${input.expression}) = ${result}` ``
- `str(result)` → `String(result)`

### Output
- `print(x)` → `console.log(x)`
- `print(chunk, end="", flush=True)` → `process.stdout.write(chunk)`
- `print()` (empty newline) → `console.log()`

### Streaming
- `client.messages.create(**{..., "stream": True})` → `await client.messages.create({ ..., stream: true })`
- `for event in stream:` → `for await (const event of stream)`
- `event.type == "content_block_delta"` → `event.type === "content_block_delta"`
- `event.delta.type == "text_delta"` → `event.delta.type === "text_delta"`
- `event.delta.text` → `event.delta.text`
- `client.messages.stream(...)` context manager → `const stream = client.messages.stream(...)`
- `for text in stream.text_stream:` → `for await (const chunk of stream.textStream)`
- `stream.get_final_message()` → `await stream.finalMessage()`

### Tool use (agentic loop)
- `tools = [{ "name": ..., "input_schema": ... }]` → `const tools: Anthropic.Tool[] = [{ name: ..., input_schema: ... }]`
- `tool_block = next(b for b in res.content if b.type == "tool_use")` →
  `const toolBlock = res.content.find((b): b is Anthropic.ToolUseBlock => b.type === "tool_use")!`
- `tool_block.input["expression"]` → cast input first: `const input = toolBlock.input as { expression: string }; input.expression`
- `tool_block.id` → `toolBlock.id`
- `tool_block.name` → `toolBlock.name`
- `"tool_use_id": tool_block.id` → `tool_use_id: toolBlock.id`
- `res.stop_reason == "end_turn"` → `res.stop_reason === "end_turn"`
- `res.stop_reason == "tool_use"` → `res.stop_reason === "tool_use"`

### Top-level code structure
Wrap all executable code (everything that is not import statements, const declarations, or function definitions) inside an `async main()` function. Add `main()` at the bottom:

```typescript
const main = async () => {
    // all executable code here
};

main();
```

### Preserve everything else
- Keep all comments exactly as written (translate `#` comments to `//` comments)
- Keep the same section headers and learning notes
- Keep the same variable names (converted to camelCase where appropriate: `tool_block` → `toolBlock`, `user_input` → `userInput`, `full_response` → `fullResponse`)
- Keep commented-out code blocks commented out in TypeScript syntax (`//` instead of `#`)