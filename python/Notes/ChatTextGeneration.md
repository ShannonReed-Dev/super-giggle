# Chat Text Generation

> When Claude processes your text, the first thing it does is break it into smaller chunks called tokens

> When you send Claude a prompt like "What do you think?", it goes through three key steps:

- **Tokenization** : Breaking your input into smaller chunks
- **Prediction** : Calculating probabilities for possible next words
- **Sampling** : Choosing a token based on those probabilities

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623338%2F03_-_008_-_Temperature_00.1748623338635.png)

>  Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this entire process to build complete sentences. The chart below is still the same probabilities just in a chart to understand it better

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623339%2F03_-_008_-_Temperature_05.1748623339740.png)

> One way we can directly influence these probabilities and control which token Claude might actually decide to select, is to use a parameter called temperature. Temperature is one of the most practical parameters you can adjust to fine-tune Claude's behavior for your specific needs.

---

## What Temperature Does

> Temperature is a powerful parameter that controls how predictable or creative Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications. Temperature is a decimal value between 0 and 1 that directly influences these selection probabilities. It's like adjusting the "creativity dial" on Claude's responses.


- Temperature is a decimal value between 0 and 1 that we provide when we make our model call
- At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token
- At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs

> At 0 the highest initial probability is more likely to occur, as the temperature increases it increases the chances that a token with a lower initial probability will be selected

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623340%2F03_-_008_-_Temperature_06.1748623340446.png)


> At temperature 0.0, "about" gets 100% probability - completely deterministic. At temperature 1.0, probabilities spread more evenly across all possible tokens, introducing randomness and creativity.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623341%2F03_-_008_-_Temperature_07.1748623341049.png)


---
## Choosing the Right Temperature

> Different tasks call for different temperature ranges. Lower temperatures for more deterministic and less creative and random results. Higher temperatures for more creative and random result.
### Low Temperature (0.0 - 0.3)

> For when want a very deterministic output and you do not need a lot of randomness or creativity

- Factual responses
- Coding assistance
- Data extraction
- Content moderation

### Medium Temperature (0.4 - 0.7)

- Summarization
- Educational content
- Problem-solving
- Creative writing with constraints

### High Temperature (0.8 - 1.0)

> For really creative focused tasks

- Brainstorming
- Creative writing
- Marketing content
- Joke generation

> Temperature doesn't guarantee different outputs, it just changes the probability of getting them. Even at high temperatures, Claude might occasionally produce similar responses. The key is matching your temperature choice to your specific use case:

- Need consistent, factual responses? Use low temperature
- Want creative brainstorming? Dial up the temperature
- Somewhere in between? Medium temperatures work well for most general tasks
---

## Implementing Temperature in Code

- Add temperature support to the `create()` function
- Low temperature : more predictable
- High temperature : more creative 

---

#### Example

> Here the temperature is added to the `chat()` function that uses the `create()` function.
>  `temperature=1.0` is added as a parameter and `"temperature": temperature` is included in the params dictionary.

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```






---



Here is the comparison between the two approaches:

| |Manual parsing|SDK simplified|
|---|---|---|
|Method|`client.messages.create(stream=True)`|`client.messages.stream()`|
|Getting text|Check `event.type` and `event.delta.type` yourself|Iterate `stream.text_stream`|
|Full response object|Build `full_response` string manually|`stream.get_final_message()`|
|Connection cleanup|You manage it|`with` block handles it automatically|

**When to use each:**

- **SDK simplified** is what you reach for by default. Less code, no chance of accidentally processing the wrong event type.
- **Manual parsing** is what you need when you want to react to specific events like `message_start` or `message_delta` (for usage/token counts), or when building tool-use streaming where you need to detect tool call deltas separately from text deltas.

