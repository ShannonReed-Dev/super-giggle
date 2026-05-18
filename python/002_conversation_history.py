from dotenv import load_dotenv
from anthropic import Anthropic

#================================================
# a script that prints exactly what fields res contains after a basic call
# Teaches: what the API actually returns vs. what developers often assume it returns
# Level: Beginner
#================================================
#Load env Variables----------------------------------------------------
load_dotenv()

# Create Client-------------------------------------------------------
client = Anthropic()
model = "claude-haiku-4-5"


# messages = []
# messages.append(
#     {
#     "role": "user",
#     "content": "What is blockchain? Answer in one sentence"
#   }
# )

# res = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=messages,
# )


# # This will print the full response object, which includes metadata and the assistant's response.
# print(res) 


# # This will print the assistant's response, which should be a one-sentence answer to the question "What is blockchain?"
# print(res.content)

# # This will print the text of the first message in the assistant's response, which should be the same one-sentence answer to the question "What is blockchain?"
# print(res.content[0].text)

#===================================================================================================================================================================================================

# TODO 1: Start with an empty messages list
messages = [] # your conversation memory


while True:
    # TODO 2: In a loop, take user input from the terminal
    user_input = input("What do you want to ask Claude? ")

    # If no exit condition, while True with no break means the only way out is Ctrl+C
    # Adding this right after taking user input before the append because you do not
    # want to append an exit command to the messages list and send it to the API
    # A common pattern is to check for a quit command:
    if user_input.lower() in ("exit", "quit", "q"):
        break

    # TODO 3: Append the user input to the messages list as a user message
    messages.append({"role": "user", "content": user_input})

    # TODO 4 : Call API with the messages list
    res = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages
    )

    assistant_response = res.content[0].text

    # TODO 5: Append the assistant reply to the messages list as an assistant message
    messages.append({"role": "assistant", "content": assistant_response})

    # TODO 6: Print the assistant's reply to the terminal
    print(assistant_response)