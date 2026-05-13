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

> You can start with a prompt that is extremely simple, which means it does not include any formatting instructions, so Claude will likely return more verbose output but this can be refined later as you iterate on your prompt design.

---

## The run_test_case Function

>This function orchestrates running a single test case and grading the result:

```python
def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # TODO - Grading
    score = 10
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }
```

> Using a hardcoded score of 10 because this placeholder lets us test the overall pipeline.

---

## The run_eval Function

> This function coordinates the entire evaluation process:

```python
def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    return results
```

> This function processes every test case in your dataset and collects all the results into a single list.

---

> Once you complete then then you would have successfully built the core evaluation pipeline

> You should be able to take your dataset, process it through Claude, and collect structured results

> The major missing piece is the grading system - that hardcoded score of 10 needs to be replaced with actual evaluation logic.

> This pipeline represents the foundation of most AI evaluation systems. While it may seem simple, you've just built the majority of what an eval pipeline actually does. 

> The complexity comes in the details - better prompts, sophisticated grading, and performance optimizations.

> The next critical step is to transform your hardcoded scores into meaningful evaluations of Claude's performance.