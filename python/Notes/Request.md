# Request anatomy

> To send a request to Claude's API you must include 4 things API key, model name, messages, and max tokens

---

## API KEY
> The anthropic Python library(SDK) is designed to automatically look for an environment variable named ANTHROPIC_API_KEY on your system

- You should keep your API key inside a `.env` file inside your project folder
- Use the `python-dotenv` library to load the key from the `.env` file into the environment in the background

> The Anthropic library has a "search" logic built into it. When you initialize the client without passing a key, it essentially does this:
- Step A: Is there a key passed in the code? No.
- Step B: Check `os.environ` for `ANTHROPIC_API_KEY`. Yes!
  - because `load_dotenv()` put it there
  - no need to write `os.environ` yourself because the Anthropic library does that work for you "under the hood."
- Step C: Use that key to authenticate.

---

## Messages

> The conversation history between you and Claude
- an array of messages representing the conversation history
- There are two types of messages:
  - *User messages* : Content you want to send to Claude (written by humans)
  - *Assistant messages* : Responses that Claude has generated
- Each message is a dictionary with a role (either "user" or "assistant") and content (the actual text)
```python
messages=[
        {
        "role": "user",
        "content": "What is vibe coding? Answer in one sentence"
        }

    ]
```
---

## Model Name
> The name of the Claude model you want to use

---

## Max Tokens
> A safety limit on response length (not a target)
- the `max_tokens` parameter acts as a safety mechanism
- if you set it to 1000, Claude will stop generating after 1000 tokens even if it has more to say
- Claude doesn't try to reach this limit, it just writes what it thinks is appropriate and stops if it hits the maximum

## Example

```python
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()# This is how anthropic gets the API key

client = Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=2048,
    messages=[
        {        
          "role": "user",
          "content": "What is vibe coding? Answer in one sentence"
        }
    ]
)
```

### Extracting the Response
> The response object contains a lot of information, but you usually just want the generated text. `message.content[0].text`, to get a clean, readable output