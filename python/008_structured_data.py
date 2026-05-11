from dotenv import load_dotenv
from anthropic import Anthropic


#================================================
# Structured Data
# Use message prfilling and stop sequences only to get three different commands in a single response
# There should not be any comments or explanation
#================================================


load_dotenv()


client = Anthropic()
model = "claude-haiku-4-5"


# Helper Functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "stop_sequences" : stop_sequences
    }

    message = client.messages.create(**params)
    print(message.content[0].text)

messages = []

prompt = """
Generate three different sample AWS CLI commands. Each should be very short.
"""

#===========================================================
# add_user_message(messages, prompt)

# res = chat(messages)

# print(res.strip())
#===========================================================



#===========================================================
# Use message prfilling and stop sequences only to get three different commands in a single response
# There should not be any comments or explanation
#===========================================================
add_user_message(messages, prompt)

# Message prefilling is not just limited to characters
add_assistant_message(messages, "Here are all three commands in a single block without any comments :\n```bash")
chat(messages, stop_sequences=["```"])

