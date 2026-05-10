# super-giggle

A learning project for the Anthropic/Claude API. Each file teaches one concept, with equivalent implementations in both Python and TypeScript.

## Project Structure

```
super-giggle/
├── python/               # Python examples using the anthropic SDK
│   ├── Notes/            # Concept reference notes (.md files)
│   └── .venv/            # Python virtual environment (ignore)
├── typescript/           # TypeScript examples using @anthropic-ai/sdk
│   └── node_modules/     # Node dependencies (ignore)
└── .claude/commands/     # Project slash commands
```

## Learning Files

Each numbered file builds on the previous one. The `d1_` prefix means Day 1 exercises.

| File | Concept |
|---|---|
| `001_requests` | Making a basic API request with `client.messages.create()` |
| `002_multi-turn-conversations` | Building a messages list for multi-turn conversations |
| `003_looping_chatbot` | A `while True` chatbot loop with user input |
| `004_system_prompting` | Passing a system prompt as an optional parameter |
| `005_temperature` | Controlling response randomness with the `temperature` parameter |
| `006_response_streaming` | Streaming responses: raw events, manual parsing, SDK simplified |
| `d1_1_agentic_loop` | Agentic loop lifecycle with tool use (4-stage pattern) |

## Running Files

**Python** (from the `python/` folder):
```
python 001_requests.py
```

**TypeScript** (from the `typescript/` folder, after `npm install`):
```
npx ts-node 001_requests.ts
```

## Slash Commands

| Command | What it does |
|---|---|
| `/convertpytots <filename(s)>` | Converts Python file(s) from `python/` to TypeScript in `typescript/` |
| `/converttstopy <filename(s)>` | Converts TypeScript file(s) from `typescript/` to Python in `python/` |

Filenames can be passed with or without their extension. Multiple files are space-separated.

Examples:
```
/convertpytots 001_requests.py
/convertpytots 001_requests.py 002_multi-turn-conversations.py
/converttstopy d1_1_agentic_loop.ts
```

## Key Patterns

**Agentic loop stop reasons:**
- `"tool_use"` - Claude wants to call a tool, execute it and loop again
- `"end_turn"` - Claude is done, print the final answer and break

**Streaming event types to know:**
- `content_block_delta` + `text_delta` - the actual text chunk to display
- Everything else is bookkeeping (start/stop events)

**Security note:** `eval()` in the agentic loop examples is for learning only. Production code should use a safe math parser.

## Environment

Both folders expect a `.env` file with `ANTHROPIC_API_KEY=your_key_here` in the project root or their respective folder.
