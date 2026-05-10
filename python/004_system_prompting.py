#Load env Variables----------------------------------------------------
from dotenv import load_dotenv
from anthropic import Anthropic


#================================================
# System Prompting
#================================================

load_dotenv()


# Create Client-------------------------------------------------------
client = Anthropic()
model = "claude-haiku-4-5"


# Helper Functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


# #--------------------------------------------------------------------------------------Hard Coded System Prompt------------------------------------------------------------------
# # Makes Request-----------------------
# def chat(messages):

#     # Create the prompt
#     system_prompt = """
#         You are a patient math tutor.
#         Do not directly answer a student's questions.
#         Guide them to a solution step by step.
#         """

#     message = client.messages.create(
#         model=model,
#         max_tokens=1000,
#         messages=messages,
#         system=system_prompt # pass the prompt to the create function
#     )
#     return message.content[0].text
# #----------------------------------------------------------------------------------------------



# messages = [] # message list

# # Use a `while True` loop to run chatbot forever
# while True:
#     # Get user input
#     user_input = input ("> ")
#     print("> ", user_input)

#     # Add user input to list of messages
#     add_user_message(messages, user_input)

#     # Get Claude's response by calling claude withthe chat function
#     answer = chat(messages)

#     # Add Claude's response to the list of meassages
#     add_assistant_message(messages, answer)

#     print("--------")
#     print(answer)



#-------------------------------------------------------------------------------------- System Prompt as argument------------------------------------------------------------------
# Makes Request-----------------------
def chat(messages, prompt=None):

# Doing it this way will allow you to call chat without a prompt if you want
# So both of these work
    # answer = chat(messages, tutor_prompt)
    # answer = chat(messages)


    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if prompt:
        params["system"] = prompt

    message = client.messages.create(**params)
    return message.content[0].text
#----------------------------------------------------------------------------------------------

# Create the prompt
senior_engineer_prompt = """
    You are a senior Python engineer. When asked to write a function, respond with only the function implementation. No prose, no explanations, no usage examples, no comments unless logic is non-obvious, no surrounding markdown commentary.

    Rules:
    - Output only the code block containing the function (and required imports).
    - Use the most concise idiomatic Python that meets the request.
    - Include type hints and a one-line docstring; omit everything else.
    - Do not restate the task, summarize the code, or suggest improvements.
    - If the request is ambiguous, ask one short clarifying question instead of guessing.
    """

messages = [] # message list

# Use a `while True` loop to run chatbot forever
while True:
    user_input = input ("> ")
    print("> ", user_input)

    add_user_message(messages, user_input)

    answer = chat(messages, senior_engineer_prompt)


    add_assistant_message(messages, answer)

    print("--------")
    print(answer)
