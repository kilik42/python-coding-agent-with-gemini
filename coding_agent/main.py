import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    

    load_dotenv()  # Load environment variables from a .env file if present
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("i need a prompt")
        
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Hello, world!"


    response = client.models.generate_content(
        ##free tier model
        model='gemini-2.0-flash-001', 
        contents='Why is the sky blue?'
    )
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
    else:
        print(f"prompt_tokens: {response.usage_metadata.prompt_token_count}, ")
        print(f"response_tokens: {response.usage_metadata.candidates_token_count}, ")

if __name__ == "__main__":
    main()