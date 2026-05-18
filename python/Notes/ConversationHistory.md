# Conversation History

#### The Anthropic API does not own your conversation history. You do.

> When you call client.messages.create(messages=[...]), you are sending the full conversation context with every request.

```python
messages = []
messages.append(
    {
    "role": "user",
    "content": "What is blockchain? Answer in one sentence"
  }
)

res = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
)


print(res)

```

> The API reads it, generates the next assistant turn, and returns only that new turn in `res`
- It does not echo back the messages you sent, and it stores nothing between calls.

```python
Message(id='msg_01HoYjZwzSfFqkW9o5RTq2dv', container=None, content=[TextBlock(citations=None, text='Blockchain is a distributed digital ledger that records transactions across multiple computers in a secure, transparent, and immutable way using cryptographic links between data blocks.', type='text')], model='claude-haiku-4-5-20251001', role='assistant', stop_details=None, stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(cache_creation=CacheCreation(ephemeral_1h_input_tokens=0, ephemeral_5m_input_tokens=0), cache_creation_input_tokens=0, cache_read_input_tokens=0, inference_geo='not_available', input_tokens=15, output_tokens=35, server_tool_use=None, service_tier='standard'))
```

> So `res.content` is a list of content blocks that only contains the new assistant turn that was generated in response to your messages. It does not contain the full conversation history.

```python
[TextBlock(citations=None, text='Blockchain is a distributed digital ledger that records transactions across multiple computers in a secure, transparent, and immutable way using cryptographic links between data blocks.', type='text')]
```

>  Your local messages list is the source of truth for the full conversation. If you want it to grow, you have to append to it yourself after each call.

> Your local messages list is the source of truth for the full conversation. If you want it to grow, you have to append to it yourself after each call.

### Muti-turn conversations Loop

> The API expects alternating user / assistant turns, so appending with "role": "assistant" is what tells Claude "this is what I already said" on the next call.

**Every time you call the API, the flow is:**
1. Append user message to messages list
2. Call API with full messages list
3. Extract assistant reply from res
4. Append assistant reply to messages list
    - this is what is missing from the code snippet above! You have to do this part yourself if you want to maintain conversation history
5. Repeat

> `res.content` is a list of content blocks, [0] gets the first one, and .text pulls the string out of it. So the append looks like this:

`messages.append({"role": "assistant", "content": res.content[0].text})`

```python
messages = [] # your conversation memory


while True:
    # TODO 2: In a loop, take user input from the terminal
    user_input = input("What do you want to ask Claude? ")

    # If no exit condition, while True with no break means the only way out is Ctrl+C
    # Adding this right after taking user input before the append because you do not
    # want to append an exit command to the messages list and send it to the API
    # A common pattern is to check for a quit command:
    if user_input.lower() in ("exit", "quit", "q"):
        break

    # TODO 3: Append the user input to the messages list as a user message
    messages.append({"role": "user", "content": user_input})

    # TODO 4 : Call API with the messages list
    res = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
    )

    assistant_response = res.content[0].text

    # TODO 5: Append the assistant reply to the messages list as an assistant message
    messages.append({"role": "assistant", "content": assistant_response})

    # TODO 6: Print the assistant's reply to the terminal
    print(assistant_response)

```
> Two questions from the user, two replies from Claude and messages will contain 4 items, alternating user/assistant, user/assistant.

```python
[{'role': 'user', 'content': 'What is a car? Answer in one sentence'}, 
 {'role': 'assistant', 'content': 'A car is a wheeled motor vehicle used for transportation.'},
 {'role': 'user', 'content': 'Do they come in different colors?'}, 
 {'role': 'assistant', 'content': 'Yes, cars come in many different colors including white, black, silver, red, blue, gray, and many other hues..'}]
```

> That is the full conversation history your script is sending on the second API call. Claude sees all 4 of those when generating its second reply, which is why it can reference what was said earlier in the conversation.

# Summary

|Pattern|Worth memorizing|
|---|---|
|`messages.append({"role": "assistant", "content": res.content[0].text})`|Yes. This is the line that maintains conversation state.|
|Alternating user/assistant roles|Yes. The API requires this structure.|
|The API returns only the new turn, not the full history|Yes. You own the history, not the server.|


--- 

##### The natural next thing to explore from here is tool use.

> When Claude calls a tool, the message you append back is shaped differently (it includes the tool result, not just text).
