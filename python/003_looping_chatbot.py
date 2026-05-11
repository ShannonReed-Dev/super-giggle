#Load env Variables----------------------------------------------------
from dotenv import load_dotenv
from anthropic import Anthropic

#================================================
# Looping Chatbot
# 1. Prompt the user to enter some input
# 2. Add the user input to the list of messages
# 3. Call the API
# 4. Add generated text to the list of messages
# 5. Print the generated text
# 6. Repeat
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
while True:# 6. Repeat
    # 1. Prompt the user to enter some input
    user_input = input ("> ")
    print("> ", user_input)

    # 2. Add the user input to the list of messages
    add_user_message(messages, user_input)

    # 3. Call the API
    answer = chat(messages)

    # 4. Add generated text to the list of messages
    add_assistant_message(messages, answer)

    # 5. Print the generated text
    print("--------")
    print(answer)
