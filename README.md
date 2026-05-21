> This is a **learning project for the Anthropic Claude API**, structured as a side-by-side Python and TypeScript tutorial.

## Getting Started

### 1. Prerequisites

| Tool | Version | Used by |
|---|---|---|
| Python | 3.10+ | `python/` examples |
| Node.js | 18+ | `typescript/` examples |
| Anthropic API key | from [console.anthropic.com](https://console.anthropic.com/) | both |

### 2. Clone and add your API key

```
git clone <repo-url>
cd super-giggle
```

Create a `.env` file in **both** `python/` and `typescript/` (or one in the project root) containing:

```
ANTHROPIC_API_KEY=your_key_here
```

### 3. Set up Python

From the `python/` folder:

```
python -m venv .venv
.venv\Scripts\activate        # Windows PowerShell
pip install anthropic python-dotenv
```

Run any example:

```
python 001_requests.py
```

### 4. Set up TypeScript

From the `typescript/` folder:

```
npm install
```

Run any example:

```
npx ts-node 001_requests.ts
```

### 5. Pick your path

Start with `001_requests` in whichever language you prefer, then work through the files in order. Each one introduces a single new concept on top of the previous.

## Structure

|Folder|Purpose|
|---|---|
|[python/](vscode-webview://0bqq8jb6ql2at4ciikjb7ldvnaqsa14tgscustm5489t054pem3r/python/)|Examples using the `anthropic` Python SDK|
|[typescript/](vscode-webview://0bqq8jb6ql2at4ciikjb7ldvnaqsa14tgscustm5489t054pem3r/typescript/)|Equivalent examples using `@anthropic-ai/sdk`|
|[.claude/commands/](vscode-webview://0bqq8jb6ql2at4ciikjb7ldvnaqsa14tgscustm5489t054pem3r/.claude/commands/)|Project slash commands for converting between the two|

## Learning Progression

Each numbered file teaches one concept and builds on the previous:

- **001** Basic API requests with `client.messages.create()`
- **002** Multi-turn conversations via a messages list
- **003** A `while True` chatbot loop
- **004** System prompts
- **005** Temperature control
- **006** Response streaming (raw events, manual parsing, SDK helper), the file you currently have open
- **007–008** Structured data output via assistant prefilling and stop sequences
- **d1_1** Agentic loop with tool use (the 4-stage pattern)

## Workflow Helpers

Two custom slash commands keep the Python and TypeScript sides in sync:

- `/convertpytots <file>` ports Python → TypeScript
- `/converttstopy <file>` ports TypeScript → Python

## Setup

Both folders expect an `.env` with `ANTHROPIC_API_KEY`. Python runs from its `.venv`, TypeScript from `node_modules` after `npm install`.

In short: a sandbox for learning Claude API concepts one feature at a time, with matched implementations in two languages.
---

# Accessing Claude/Anthropic API

> Helps with familiarizing yourself with the terminology and overall process you'll encounter when working with Claude's API 

## Topic Covered
- Accessing the API
- Getting an API key
- Making a request
- Conversation history
- Multi-Turn conversations
- Chat exercise
- System prompts
- System prompts exercise
- Temperature
- Response streaming
- Structured data

---






