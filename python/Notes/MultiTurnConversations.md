# Multi-Turn Conversations

> You ask Claude "What is pizza?" and it answers. Then you ask "What toppings are popular?" but Claude doesn't understand what you're referring to, it doesn't remember previous messages, fix this by creating multi-turn conversations

---

## Crucial Concept

> Claude doesn't store any of your conversation history. 

> Each request you make is completely independent, with no memory of previous exchanges.

> You can have a multi-turn conversation where Claude remembers context from earlier messages. You do this by handling the conversation state/context yourself and you need two things to do that

- Manually maintain a list of all messages in your code
- Send the complete message history with every request

### Here's the flow that actually works:

1. Send your initial user message to Claude
2. Take Claude's response and add it to your message list as an assistant message
3. Add your follow-up question as another user message
4. Send the entire conversation history to Claude

---
## Conversation Management

> To make conversation management easier, you can create three helper functions, then use them to maintain a conversation history

```python
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)

```

> Claude will understand that "Write another sentence" refers to expanding on the quantum computing definition, because you've provided the complete conversation context.

> These helper functions will be useful throughout your work with Claude, making it much easier to build applications that can maintain meaningful conversations over multiple exchanges.