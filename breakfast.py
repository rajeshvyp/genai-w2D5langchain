from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the API key from env file
load_dotenv()

# Create the LangChain model
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Suggest exactly 5 healthy breakfast ideas.
Number them from 1 to 5, one idea per line.
Do not include an introduction or conclusion.
Keep each idea short and practical.
"""

# Get the response
reply = llm.invoke(prompt)

# Print only the response text
print(reply.content)