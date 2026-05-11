# System Prompts
> System prompts are a powerful way to customize how Claude responds to user input. They are essential for creating AI applications that behave consistently and appropriately for their intended purpose. They transform generic AI responses into specialized, role-appropriate interactions.

- A system prompt is a separate instruction channel that tells Claude **who it is** and **how it should behave** before any user message arrives.
  - System prompts provide Claude guidance on how to respond
  - Claude will try to respond in the same way someone in the specified role would respond
  - Helps keep Claude on task
- Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case
- Influences how Claude responds throughout the conversation, like setting Claude's personality and expertise for the entire interaction.
- It is delivered through a dedicated top-level parameter on the request, not inside the `messages` array.
- This separation is intentional: user turns describe **the task**, the system prompt describes **the operator**.

---
## Defining System Prompts
> Defined them as plain strings and pass them into the create function call.

```python
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)

```

### Flexible Chat Function
> Rather than hard-coding system prompts, you can make your chat function more reusable by accepting system prompts as parameters
- **IMPORTANT DETAIL** :Claude's API doesn't accept `system=None`, so you need to conditionally include the system parameter only when it's provided
- Then you can call your chat function with or without a system prompt

```python
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)

```


## Why it matters

|Benefit|What it gives you|
|---|---|
|Role grounding|Turns Claude from a generalist into a domain expert (legal analyst, code reviewer, support agent)|
|Tone control|Locks in voice and register across every turn without repeating yourself|
|Behavioral guardrails|Sets refusals, formatting rules, and scope limits that persist for the whole conversation|
|Token efficiency|Instructions live once at the top instead of being repeated in every user message|
|Cacheability|Pairs cleanly with prompt caching, since the system block is stable across turns|

- Role prompting is the most powerful way to use system prompts with Claude
  - can deliver enhanced accuracy in complex scenarios like legal analysis or financial modeling, tailored tone, and improved focus by keeping Claude within the bounds of the task's specific requirements


## What Belongs in the system prompt
- Role and identity ("You are a senior frontend engineer reviewing React code")
- Domain expertise and audience
- Tone, voice, output format rules
- Persistent constraints and refusals
- Tool usage policy (when tools are configured)

## What Belongs in the user turn
- The actual task or question
- Dynamic data (datasets, document contents, user input)
- Per-request parameters that change every call

## A well-structured system prompt typically layers four things

```
You are a [role].
You are an expert in [domain] and respond to [audience] in a [style] manner.

<instructions>
  Step-by-step process Claude should follow.
</instructions>

<rules>
  Hard constraints. What to do, what to refuse.
</rules>

<output_format>
  Exact shape of the response.
</output_format>
```

- Structured instructions wrapped in `<instructions>`, `<context>`, `<rules>` tags help Claude identify sections accurately
- Affirmative phrasing like "Explain in prose paragraphs" is more reliable than negative phrasing like "don't use bullet points." 

- [Claude Lab: System Prompt Design Guide](https://claudelab.net/en/articles/claude-ai/system-prompt-design)

## Important nuances

1. **System prompts are not hidden from Claude.** They influence every response, but if a user asks Claude to reveal them, it might. Do not put secrets, API keys, or sensitive logic there.
2. **API system prompts are yours alone.** The system prompts published for claude.ai and the iOS and Android apps do not apply to the Claude API. When you build on the API, you author the entire behavioral layer from scratch. 
3. **They count toward your context window.** Long system prompts cost tokens on every request, which is one reason prompt caching exists.
4. **Multi-turn context still requires resending.** The system prompt persists across a single API call, but Claude has no server-side memory between calls. Each request must include the full `messages` history plus the system prompt.


## System Prompts Are The Foundation of
- Tool definitions reference behaviors set up in the system prompt
- Agentic workflows use it to scope each subagent's role
- RAG implementations use it to constrain how retrieved context is handle

