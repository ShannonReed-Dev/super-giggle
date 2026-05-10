from dotenv import load_dotenv
from anthropic import Anthropic


#================================================
# Temperature
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


def chat(messages, prompt=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if prompt:
        params["system"] = prompt

    message = client.messages.create(**params)
    return message.content[0].text


book_idea_prompt = """
    Generate a one sentence book idea for kids under between the ages 8 and 10
    """

messages = []

add_user_message(messages, book_idea_prompt)

answer = chat(messages, temperature=0.0 )

print(answer)


# with temperature=0.0 I always seem to got something about, A young girl discovers that her grandmother's antique music box over and over
    # A young girl discovers that her grandmother's antique music box opens 
    # a magical portal to a hidden kingdom where forgotten fairy tales 
    # are real, and she must help the storybook characters fix 
    # their mixed-up endings before the magic disappears forever.

    # A young girl discovers that her grandmother's antique music box opens a 
    # magical portal to a hidden kingdom where forgotten fairy tales are real, 
    # and she must help the storybook characters fix their mixed-up 
    # endings before the magic disappears forever.

# Just because you dial up the temperature does not mean you will get dramictically different results
# It just increase the chances of getting a different one


# with temperature=1.0, i kept getting something about a magical library and a grandmother
# after running a few time i finally got a dramatic different one about stars disappearing from the night


    # When 10-year-old Maya discovers a hidden library behind her grandmother's bookshelf where the 
    # characters from books come to life, she must help them escape a mischievous villain who's 
    # trapping them inside their stories.

    # **"The Secret Map to the Lost Library"** follows a curious fourth-grader who discovers an old 
    # map in her grandmother's attic that leads to a magical hidden library where the books come alive, 
    # and she must solve riddles and puzzles to find the one book that can save her town from 
    # forgetting its history.

    # When a shy fourth-grader discovers that her grandmother's old attic is actually a portal to 
    # a magical library where books come to life, she must team up with characters from her 
    # favorite stories to stop a villain from erasing all the happy endings.

    # When a curious 9-year-old discovers that stars are disappearing from the night sky one by one, 
    # she must team up with her friends and a wise old astronomer to solve the cosmic mystery 
    # before darkness covers the world forever.