# LLMs : Stop Sequences

> `stop_sequences` are set of characters (like a word, symbol, or newline) that tells the AI exactly when to stop talking.


> It's like a "safe word" for your API call—the moment the AI generates that specific string, it immediately cuts off its response.


---

> `stop_sequences` is a widely supported concept across LLM providers, though the parameter name varies slightly:

|Provider|Parameter Name|Example|
|---|---|---|
|Anthropic|`stop_sequences`|`stop_sequences=["END", "STOP"]`|
|OpenAI|`stop`|`stop=["END", "STOP"]`|
|Google Gemini|`stop_sequences`|same pattern|
|Cohere|`stop_sequences`|same pattern|

> The underlying idea is universal: before generating each token, the model checks whether the output so far ends with one of your stop strings. If yes, generation halts and that string is **not** included in the response.

> The concept predates the API era entirely. It comes from how text generation works at the inference level, and most inference engines expose it.

---

# How It Works Under the Hood
- When you send a request to an API (like OpenAI or Anthropic), the model generates text token by token. 
- With a stop sequence configured:
    - Continuous Monitoring: After generating each token, the API checks if the current tail of the text matches any of your defined stop sequences.
    - Immediate Termination: If a match is found, the generation process halts instantly, even if the model hasn't reached its maximum token limit.
    - Automatic Cleanup: The stop sequence itself is typically omitted from the final text returned to you, so the output stays clean.

---

# Why Use Them?
> Stop sequences are essential for maintaining structure and saving money. Common use cases include:

- Preventing "Hallucinated" Conversations: In a chatbot scenario, you might set User: as a stop sequence. This prevents the AI from getting carried away and writing both sides of the dialogue.
- Structured Data: If you only want a single line of text, you can use \n (a newline) as a stop sequence to ensure the model doesn't start a second paragraph.
- Cost Control: Since you pay per token, stopping the model as soon as it provides the answer saves you from paying for unnecessary "yapping" or filler text.
- Ending Lists: You can set a number or a specific character (like a closing bracket }) as a stop sequence to terminate a JSON object exactly where it should end.

---
# Examples 

> Most APIs allow you to provide up to four different stop sequences in a single request

| Goal                                         | Stop Sequence Example |
| -------------------------------------------- | --------------------- |
| **End a single-line reply**                  | `\n`                  |
| **Stop a Q&A bot from asking new questions** | `Q:` or `Question:`   |
| **End a code block**                         | ` ``` `               |
| **Stop a chat turn**                         | `Human:` or `User:`   |
