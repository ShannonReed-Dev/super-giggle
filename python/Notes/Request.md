# Request anatomy

> To send a request to Claude's API you must include API key, model name, messages, and max tokens

Every API call to the Messages endpoint bundles four core pieces:

1. `model` : which Claude variant runs the request
2. `system` : the system prompt (string or content blocks)
3. `messages` : the conversation history with `user` and `assistant` roles
4. `max_tokens` : response length cap

> When you send a request to Claude, you package the model, a system prompt that defines Claude's behavior, an array of messages representing the conversation history, and a `max_tokens` limit for the response length.



## Minimal Example
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=2048,
    system="You are a seasoned data scientist at a Fortune 500 company.",
    messages=[
        {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
    ]
)
```

- The system parameter is used to set Claude's role, while task-specific instructions go in the user turn
- That split is the single most important convention to internalize


---
## System Prompts

> When you want responses in a certain format use system prompts explaining the role and what you want it to do

> System prompts are a powerful way to customize how Claude responds to user input. Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case.


### What a system prompt is

> A system prompt is a separate instruction channel that tells Claude _who it is_ and _how it should behave_ before any user message arrives.

- Influences how Claude responds throughout the conversation, like setting Claude's personality and expertise for the entire interaction.

> It is delivered through a dedicated top-level parameter on the request, not inside the `messages` array.

- This separation is intentional: user turns describe _the task_, the system prompt describes _the operator_.


#### Why it matters

|Benefit|What it gives you|
|---|---|
|Role grounding|Turns Claude from a generalist into a domain expert (legal analyst, code reviewer, support agent)|
|Tone control|Locks in voice and register across every turn without repeating yourself|
|Behavioral guardrails|Sets refusals, formatting rules, and scope limits that persist for the whole conversation|
|Token efficiency|Instructions live once at the top instead of being repeated in every user message|
|Cacheability|Pairs cleanly with prompt caching, since the system block is stable across turns|

> Role prompting is the most powerful way to use system prompts with Claude, and can deliver enhanced accuracy in complex scenarios like legal analysis or financial modeling, tailored tone, and improved focus by keeping Claude within the bounds of the task's specific requirements. 


#### What goes in vs what stays out

**Belongs in the system prompt:**

- Role and identity ("You are a senior frontend engineer reviewing React code")
- Domain expertise and audience
- Tone, voice, output format rules
- Persistent constraints and refusals
- Tool usage policy (when tools are configured)

**Belongs in the user turn:**

- The actual task or question
- Dynamic data (datasets, document contents, user input)
- Per-request parameters that change every call

#### Practical patterns from the course

A well-structured system prompt typically layers four things:

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


Structured instructions wrapped in `<instructions>`, `<context>`, `<rules>` tags help Claude identify sections accurately, and affirmative phrasing like "Explain in prose paragraphs" is more reliable than negative phrasing like "don't use bullet points." [Claude Lab](https://claudelab.net/en/articles/claude-ai/system-prompt-design)

#### Important nuances

1. **System prompts are not hidden from Claude.** They influence every response, but if a user asks Claude to reveal them, it might. Do not put secrets, API keys, or sensitive logic there.
2. **API system prompts are yours alone.** The system prompts published for claude.ai and the iOS and Android apps do not apply to the Claude API. When you build on the API, you author the entire behavioral layer from scratch. 
3. **They count toward your context window.** Long system prompts cost tokens on every request, which is one reason prompt caching exists.
4. **Multi-turn context still requires resending.** The system prompt persists across a single API call, but Claude has no server-side memory between calls. Each request must include the full `messages` history plus the system prompt.


#### System Prompts Are The Foundation

- Tool definitions reference behaviors set up in the system prompt
- Agentic workflows use it to scope each subagent's role
- RAG implementations use it to constrain how retrieved context is handled

