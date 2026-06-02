> When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively.

Understanding this flow helps you:

- Design secure architectures that protect your API keys
- Set appropriate token limits for your use case
- Handle different stop reasons in your application logic
- Debug issues by understanding where they might occur in the pipeline

---

## The Five-Step Request Flow

> What happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen

Every interaction with Claude follows a predictable pattern with five distinct phases:
- Request to server
- Request to Anthropic API
- Model processing
- Response to server
- Response to client.

## You Need a Server

> You should never make requests to the Anthropic API directly from client-side code

- API requests require a secret API key for authentication
- Exposing this key in client code creates a serious security vulnerability
- Anyone could extract the key and make unauthorized requests

> Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

## Making API Requests

Your server can contact the Anthropic API in two ways:
- Official SDK 
	- Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby
- Plain HTTP requests

---
Every request must include these essential fields:

- **API Key** : Identifies your request to Anthropic
- **Model** : Name of the model to use (like "claude-3-sonnet")
- **Messages** : List containing the user's input text
- **Max Tokens** : Limit for how many tokens Claude can generate

---

## Processing Requests

> Once Anthropic receives your request, Claude processes it through four main stages

- Tokenization
- Embedding
- Contextualization
- Generation

### Tokenization

- User input text is broken down into smaller chunks called tokens. 
- These can be whole words, parts of words, spaces, or symbols.
- For simplicity, think of each word as one token.

### Embedding

- Each token gets converted into an embedding : a long list of numbers that represents all possible meanings of that word
- Think of embeddings as numerical definitions that capture semantic relationships

### Contextualization

> Words often have multiple meanings, we narrow down the meaning because of its position in a sentence and presence of other words around it

- Each embedding is refined based on surrounding words to determine the most likely meaning in context. 
- This process adjusts the numerical representations to highlight the appropriate definition.

### Generation

- The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. 
- Claude doesn't always pick the highest probability word, it uses a mix of probability and controlled randomness to create natural, varied responses.

> After selecting each word, Claude adds it to the sequence and repeats the entire process for the next word.

- After each token, Claude checks several conditions to decide whether to continue
	- **Max tokens reached** - Has it hit the limit you specified?
		- End Of Sequence Token(EOS) : a special signal the model uses to indicate that it has reached what it considers to be an natural end to its generation and that it should stop
	- **Natural ending** - Did it generate an end-of-sequence token?
	- **Stop sequence** - Did it encounter a predefined stop phrase?

### The API Response

> When generation completes, the API sends back a structured response

- **Message** - The generated text
- **Usage** - Count of input and output tokens
- **Stop Reason** - Why generation ended

> Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

---

### Terms

- Semantics is the study of meaning in language, focusing on how words, phrases, and sentences convey meaning, and how these meanings are structured, interpreted, and changed


----


## The 4-stage Model(per request)

> The full input-to-output path : Once Anthropic receives your request, Claude processes it through four main stages

- Tokenization
- Embedding
- Contextualization
- Generation

---
## The 3-step Model(per token during the generate stage)

> Zooms into what happens repeatedly during generation: When you send Claude a prompt like "What do you think?", it goes through three key steps:

- Tokenization : Breaking your input into smaller chunks
- Prediction : Calculating probabilities for possible next words
- Sampling : Choosing a token based on those probabilities

---

## Mnemonic

- Outer loop (per request): Tokenize → Embed → Contextualize → Generate
- Inner loop (per output token, inside Generate): Tokenize context → Predict → Sample → append → repeat until stop

---

> Both the 4-stage model and the 3-step model describe Claude's request lifecycle

- The 4-stage model = **end-to-end request flow** (one pass through the system).
- The 3-step model = **the generation loop itself**, run once per output token.
- Embedding and contextualization are the internal mechanics of what the 3-step view labels "Prediction."
- Sampling is the act inside Generation that picks the actual token from the probability distribution.
