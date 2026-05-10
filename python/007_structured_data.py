from dotenv import load_dotenv
from anthropic import Anthropic


#================================================
# Structured Data
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
    return message.content[0].text


user_message = "Count from 1 to 10"

messages = []
#===========================================================
# add_user_message(messages, user_message)

# res = chat(messages, stop_sequences=["8"] )

# print(res)

#===========================================================


# To generate structured data like JSON, Python code, or 
# bulleted lists, you'll often run into a common problem: 
    # Claude wants to be helpful and add explanatory text 
    # around your content, but sometimes you need just 
    # the raw data with nothing else.



# add_user_message(messages, "Generate a very short bridge rule as json")

# res = chat(messages)

# # Claude returns the JSON wrapped in markdown code blocks
# # with explanatory text, users can't simply copy the 
# # entire response, they have to manually select 
# # just the JSON portion
# print(res)
#===========================================================


#===========================================================
# Assistant Message Prefilling + Stop Sequences
# Combine assistant message prefilling with stop sequences 
# to get exactly the content you want
#===========================================================
add_user_message(messages, "Generate a very short bridge rule as json")

# prefilled assistant message makes Claude 
# think it already started a markdown code block
# So it thinks it already wrote out "```json",
# so it continues by writing just the JSON content
add_assistant_message(messages, "```json")

# Claude then tries to close the code block with ```, 
# but the stop sequence immediately ends generation
res = chat(messages, stop_sequences=["```"])

print(res)


#===========================================================