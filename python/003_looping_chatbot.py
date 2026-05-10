#Load env Variables----------------------------------------------------
from dotenv import load_dotenv
from anthropic import Anthropic

#================================================
# Looping Chatbot
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

# Makes Request-----------------------
def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


messages = [] # message list

# Use a `while True` loop to run chatbot forever
while True:
    # Get user input
    user_input = input ("> ")
    print("> ", user_input)

    # Add user input to list of messages
    add_user_message(messages, user_input)

    # Get Claude's response by calling claude withthe chat function
    answer = chat(messages)

    # Add Claude's response to the list of meassages
    add_assistant_message(messages, answer)

    print("--------")
    print(answer)
