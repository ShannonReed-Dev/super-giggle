# Response Streaming : Manual parsing vs SDK simplified

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