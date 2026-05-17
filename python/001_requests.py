#Load env Variables----------------------------------------------------
from dotenv import load_dotenv
from anthropic import Anthropic

#================================================
# Making Requests
#================================================

load_dotenv()


# Create Client-------------------------------------------------------


client = Anthropic()
model = "claude-haiku-4-5"


# Makw Request------------------------------------------------------
# The Create Function
# The core of making API requests is the client.messages.create() function. This function requires three key parameters:
    # model - The name of the Claude model you want to use
    # max_tokens - A safety limit on response length (not a target)
        # The max_tokens parameter acts as a safety mechanism. 
        # If you set it to 1000, Claude will stop generating after 1000 tokens even if it has more to say. 
        # Claude doesn't try to reach this limit - it just writes what it thinks is appropriate and stops if it hits the maximum.
    # messages - The conversation history you're sending to Claude
        # Messages represent the conversation between you and Claude, similar to a chat application. There are two types of messages:
            # User messages - Content you want to send to Claude (written by humans)
            # Assistant messages - Responses that Claude has generated
        # Each message is a dictionary with a role (either "user" or "assistant") and content (the actual text).

#----------------------------------------------------
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
        "role": "user",
        "content": "What is quantum computing? Answer in one sentence"
        }

    ]
)

# When you run this code, Claude will process your request and return a response object containing the generated text along with metadata about the request.



# Extracting the Response-----------------------------------------------------------
# message 
    # this response object contains a lot of information, but you usually just want 
    # the generated text  which is message.content[0].text

# print(message)


# clean, readable output 
print(message.content[0].text)