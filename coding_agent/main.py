import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # Load environment variables from a .env file if present
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



response = client.models.generate_content(
    ##free tier model
    model='gemini-2.0-flash-001', 
    contents='Why is the sky blue?'
)
print(response.text)
print(f"prompt_tokens: {response.usage_metadata.prompt_token_count}, ")
print(f"response_tokens: {response.usage_metadata.candidates_token_count}, ")