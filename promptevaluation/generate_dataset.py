# Load env variables and create client
from dotenv import load_dotenv
from anthropic import Anthropic
import json


load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"


# Helper functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text



# Dataset generation function
# Takes the prompt and sends it to claude to get back a list of tasks
def generate_dataset():
    prompt = """
Generate a evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts
that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects,
each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
    {
        "task": "Description of task",
    },
    ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a regular expression.
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

# To properly parse the JSON response, we'll use prefilling and stop sequences
    messages = []
    add_user_message(messages, prompt)# Takes the prompt and sends it to claude to get back a list of tasks
    add_assistant_message(messages, "```json")# Then parses them as json
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)


dataset = generate_dataset()
print(dataset)
# This should return three different test cases covering our target outputs 
# - Python functions, JSON configurations, and regular expressions for AWS-specific tasks.


# Once we have our dataset, we'll save it to a file so we can easily load it later during evaluation
# This creates a dataset.json file in the same directory, containing your list of tasks ready for prompt evaluation.
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)



# With this foundation in place, you now have a systematic way to 
# generate test data for evaluating how well your prompts perform across different types of AWS-related coding tasks.

