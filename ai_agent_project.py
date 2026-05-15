# -----------------------------------
# IMPORT LIBRARIES
# -----------------------------------

from openai import OpenAI
from dotenv import load_dotenv
import os


# -----------------------------------
# LOAD ENV VARIABLES
# -----------------------------------

# Load variables from .env file
load_dotenv()


# -----------------------------------
# GET API KEY
# -----------------------------------

api_key = os.getenv("OPENROUTER_API_KEY")


# -----------------------------------
# CREATE OPENAI CLIENT
# -----------------------------------

client = OpenAI(

    # API key
    api_key=api_key,

    # OpenRouter endpoint
    base_url="https://openrouter.ai/api/v1"
)


# -----------------------------------
# TAKE USER INPUT
# -----------------------------------

user_question = input("Ask Anything: ")


# -----------------------------------
# SEND REQUEST TO LLM
# -----------------------------------

response = client.chat.completions.create(

    # Free model from OpenRouter
    model="openrouter/free",

    # Conversation messages
    messages=[
        {
            "role": "user",
            "content": user_question
        }
    ]
)


# -----------------------------------
# PRINT AI RESPONSE
# -----------------------------------

print("\nAI Response:\n")

print(response.choices[0].message.content)