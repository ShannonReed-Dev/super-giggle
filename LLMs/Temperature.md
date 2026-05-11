# LLM Temperature


> LLM temperature is a parameter that controls the randomness and creativity of generated text, functioning like a "creativity knob." 

- Low temperatures (0.0-0.3) produce deterministic, focused, and precise output
- High temperatures (0.8-1.0+) lead to creative, diverse, and unpredictable text by forcing the model to choose less probable words

## Usage Scenarios (Anthropic/Other LLMs)
- Low Temperature (0.0-0.3): Use for factual Q&A, data extraction, or code generation where accuracy is essential. Note: As mentioned in the Claude API Docs, some non-determinism might still exist.
- Moderate Temperature (0.5-0.7): Balanced output for conversational AI or summarizing, offering a balance between predictability and creativity.
- High Temperature (0.8-1.0+): Use for brainstorming, fiction writing, or creative brainstorming to get unexpected, diverse ideas.

---

- 0 is not always absolute: Even with temperature at 0, some models (specifically those accessed via API) may not be perfectly deterministic.
- It controls risk: High temperature increases the likelihood of "hallucinations"—convincing but incorrect answers—because the model is not relying on the most probable, proven pathways.
- Scale: Usually measured from 0 to 2, though most effective output is found within 0-1

---

## How Temperature Works Mechanically
- Probability Distribution: LLMs predict the next word (token) based on probability. A low temperature sharpens the distribution—amplifying high-probability words (e.g., picking "lion" over "meerkat").
- Softmax Function: Temperature is a factor in the mathematical function that turns raw model scores into probabilities. High temperature flattens this distribution, giving lower-probability words a better chance to be chosen, creating more varied text.

