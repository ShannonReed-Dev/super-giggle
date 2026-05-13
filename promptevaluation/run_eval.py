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

#=====================================================================

# This function will be called with each test case
# Each json object in dataset.json is a test case
def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
        Please solve the following task:

        {test_case["task"]}
    """
    # Pass the test case to Claude
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output



# This function will call the run_prompt() function and pass it the test case
# Then grade the result and return a dictionary
def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)# call the run_prompt function and pass it the test case
    
    # TODO - Grading
    # Using hard coded score of 10 as a placeholder 
    # so the overall pipeline can be tested
    score = 10
    
    return {# grade the result and return a dictionary
        "output": output,
        "test_case": test_case,
        "score": score
    }


# The function takes the entire dataset(the entire json object)
# Then calls run_test_case(), and assemble all the results together
def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    # For every test case in the dataset 
    for test_case in dataset:
        # Pass the test case to the
        # run_test_case() function and get the result for running 
        result = run_test_case(test_case)
        # add the result to the list of results
        results.append(result)
        
    
    return results


# The dataset needs to be loaded for the evaluation
# This reads the dataset.json file 
with open('dataset.json', 'r') as f:
     dataset = json.load(f)# parses the data as json

# Pass the dataset to the run the run_eval()
# function and get the results
results = run_eval(dataset)

# the results will be a large json object
# this prints it out in a better format
print(json.dumps(results, indent=2))

# This will return a list of dictionaries/objects, where each dictionary represents
# a individual test case, the score will always be 10 because it is hardcoded