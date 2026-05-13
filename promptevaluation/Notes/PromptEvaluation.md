## Prompt Evaluation

> Automated testing to **measure** how well your prompts work it's about measuring their effectiveness through automated testing. You can:

- Test against expected answers
- Compare different versions of the same prompt
- Review outputs for errors

## Three Paths After Writing a Prompt

> Once you've drafted a prompt, you typically face three options for what to do next:


- **Option 1:** Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

- **Option 2:** Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

> Options 1 and 2 are common traps that all engineers fall into, because it's natural to write a prompt for a serious application and not test it thoroughly enough. We tend to underestimate how many edge cases real users will encounter.


- **Option 3:** Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective metrics. This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

> The reality is that when you deploy a prompt to production, users will interact with it in ways you never anticipated. What seemed like a solid prompt during your limited testing can quickly break down when faced with the full variety of real-world inputs.


## The Evaluation-First Approach

> Option 3 represents a more systematic approach to prompt development. By running your prompt through an evaluation pipeline, you get objective metrics about its performance across a broader range of test cases. This data-driven approach lets you:

- Identify weaknesses before they become production issues
- Compare different prompt versions objectively
- Iterate with confidence based on measurable improvements
- Build more reliable AI applications

> While this approach requires more upfront investment in time and testing infrastructure, it pays dividends in the reliability and robustness of your final application. The goal is to catch problems during development rather than after your users encounter them.


---

## Workflow

> A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.


### Step 1: Draft a Prompt

> Start by writing an initial prompt that you want to improve
- This prompt will serve as your baseline for testing and improvement.

```
prompt = f"""
Please answer the user's question:

{question}
"""
```


### Step 2: Create an Eval Dataset

> Your evaluation dataset contains sample inputs that represent the types of questions or requests your prompt will handle in production. The dataset should include questions that will be interpolated into your prompt template.

> Dataset that includes three questions:

- "What's 2+2?"
- "How do I make oatmeal?"
- "How far away is the Moon?"

> In real-world evaluations, you might have tens, hundreds, or even thousands of records. You can assemble these datasets by hand or use Claude to generate them for you.

### Step 3: Feed Through Claude

> Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude to get responses.

```
prompt = f"""
Please answer the user's question:

What's 2+2?
"""

```

```
prompt = f"""
Please answer the user's question:

"How do I make oatmeal?"
"""
```

```
prompt = f"""
Please answer the user's question:

"How far away is the Moon?"
"""
```

> Claude might respond with "2 + 2 = 4" for the math question, provide oatmeal cooking instructions for the second question, and give the distance to the Moon for the third.


## Step 4: Feed Through a Grader

> The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.

> The grader might assign:

- Math question: 10 (perfect answer)
- Oatmeal question: 4 (needs improvement)
- Moon question: 9 (very good answer)

> The average score across all questions gives you an objective measurement: (10 + 4 + 9) ÷ 3 = 7.66


## Step 5: Change Prompt and Repeat

> Now that you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.

- For example, you might add more guidance to your prompt:

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

> After running this improved prompt through the same evaluation process, you might get a higher average score of 8.7, indicating that the additional instruction helped Claude provide better responses.

## Prompt Scoring

The key benefit of this workflow is getting objective measurements of prompt performance. You can:

- Compare different prompt versions numerically
- Use the version with the best score
- Continue iterating to find even better approaches

> This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.


# Prompt Evaluation Flow : The Evaluation-First Approach
The key benefit of this workflow is getting objective measurements of prompt performance. You can:

- Compare different prompt versions numerically
- Use the version with the best score
- Continue iterating to find even better approaches

> This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.

- Run the prompt through an evaluation pipeline to score it
- Then iterate on the prompt based on objective metrics. 
- This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

---

## 1. Write the Prompt
    - Start by writing an initial prompt that you want to improve
    - This prompt will serve as your baseline for testing and improvement.


## 2. Create an Eval Dataset
    - Your evaluation dataset should contain sample inputs that represent the types of questions or requests your prompt will handle in production. 
    - The dataset should include questions that will be interpolated into your prompt template.
    - Assemble these datasets by hand or use Claude to generate them for you

## 3. Feed Through Claude
    - Take each question from your dataset and merge it with your prompt template to create complete prompts. 
    - Then send each one to Claude to get responses.


## 4. Feed Through a Grader
- The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. 
- This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.
- The average score across all questions gives you an objective measurement: (10 + 4 + 9) ÷ 3 = 7.66


## 5. Change Prompt and Repeat
- Once you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.
- After running the improved prompt through the same evaluation process, you might get a higher average score, indicating that the additional instruction helped Claude provide better responses.

---


# Custom prompt evaluation workflow

> Create a solid prompt and then generate test data to see how well it performs

## Setting Up the Goal

> The prompt needs to assist users in writing three specific types of output for AWS use cases:

- Python code
- JSON configuration files
- Regular expressions

> The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

### Goal
- Write a prompt that will assit users in writing Python code, JSON config, or Regular Expressions focused on AWS-specific use cases
- **Input**
    - User will ask for code for a specific task
-**Output**
    - Python,JSON, or a regular expression without any explanation

#### Version 1

```
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

### Evaluation Datasets

> An evaluation dataset contains inputs that we'll feed into the prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

> The dataset will be an array of JSON objects, where each object contains a "task" property describing what we want Claude to accomplish. We can either create this dataset by hand or generate it automatically using Claude.

#### [Generate Evaluation Datasets Example](./promptevaluation.py)

> Since we're generating test data, this is a perfect opportunity to use a faster model like Haiku instead of the full Claude model.

### Running The Evaluations

> Once you have your evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

> The evaluation process follows a clear workflow: 

- Take the dataset of test cases
- Combine each one with your prompt template
- Send it to Claude for processing
- Then evaluate the output using a grader system.

> More one the [Evaluation Process](./EvaluationProcess.md)



