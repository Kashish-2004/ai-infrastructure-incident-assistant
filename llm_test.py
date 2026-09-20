from openai import OpenAI
from dotenv import load_dotenv
import os
from vector_store import retrieve_relevant_chunk

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if (api_key):
    print("API key loaded successfully")
else:
    print("API key not found")

client= OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
    )
question = "My server has 95% disk usage because of huge logs. What should I investigate?"
retrieve_chunk,similarity_score= retrieve_relevant_chunk(question)
prompt= f"Question: {question}\nRelevant knowledge:\n{retrieve_chunk}"


response=client.responses.create(
    model="openai/gpt-oss-20b",
    input=prompt
)

print(response.output_text)