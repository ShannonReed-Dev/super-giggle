# Structured Data : Prefilled Messages and Stop Sequences

> You're building an app that needs clean JSON from Claude with no extra text or formatting. How do you get just the raw JSON?

 Combine prefilled messages and stop sequences

> When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text around your content. While this is usually great, sometimes you need just the raw data with nothing else.

## The Problem with Default Responses

> By default, when you ask Claude to generate JSON, you might get something like this:

````json
```json
{
  "bridge_rule": {
    "id": "rule_001",
    "name": "Simple Bridge",
    "condition": "source == 'A'",
    "action": "forward_to('B')",
    "enabled": true
  }
}
```

````

> The JSON is correct, but it's wrapped in markdown formatting and includes explanatory text. For a web app where users need to copy the raw JSON, this creates friction in the user experience.

## Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

```python
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
```

This technique works by:

1. The user message tells Claude what to generate
2. The prefilled assistant message makes Claude think it already started a markdown code block
3. Claude continues by writing just the JSON content
4. When Claude tries to close the code block with ` ``` `, the stop sequence immediately ends generation

> The result is clean JSON with no extra formatting:

```json
{
  "bridge_rule": {
    "id": "rule_001",
    "name": "Simple Bridge",
    "condition": "source == 'A'",
    "action": "forward_to('B')",
    "enabled": true
  }
}
```

### [Example](../007_structured_data.py)


---
> If you notice some extra newline characters in the response hese are easy to handle:

```python
import json

# Clean up and parse the JSON
clean_json = json.loads(text.strip())

```

> This technique isn't limited to JSON generation. Use it anytime you need structured data without commentary:

- Python code snippets
- Bulleted lists
- CSV data
- Any formatted content where you want just the content, not explanations

> Identify what Claude naturally wants to wrap your content in

> Then use that as your prefill and stop sequence. 

> This approach gives you precise control over Claude's output format, making it much easier to integrate AI-generated content into applications where clean, structured data is essential

---