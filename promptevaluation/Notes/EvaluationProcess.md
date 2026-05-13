# Evaluation Process

> Once you have your evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

> The evaluation process follows a clear workflow: 

- Take the dataset of test cases
- Combine each one with your prompt template
- Send it to Claude for processing
- Then evaluate the output using a grader system.

---

## Building the Core Functions

> The evaluation pipeline consists of three main functions, each with a specific responsibility. 

### The run_prompt Function

> The function that handles individual prompts, it takes a test case and merges it with your prompt template

```python
def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output
```