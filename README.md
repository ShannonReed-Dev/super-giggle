> This is a **learning project for the Anthropic Claude API**, structured as a side-by-side Python and TypeScript tutorial.

## Getting Started

### 1. Prerequisites

| Tool | Version | Used by |
|---|---|---|
| Python | 3.10+ | `python/` examples |
| Node.js | 18+ | `typescript/` examples |
| Anthropic API key | from [console.anthropic.com](https://console.anthropic.com/) | both |

### 2. Add your API key

```
cd `python/`
```

Create a `.env` file in `python/` or in the project root) containing:

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


> [START HERE](https://github.com/Python-Artificial-Intelligence/accessing-claude-via-api/blob/main/python/README.md)

