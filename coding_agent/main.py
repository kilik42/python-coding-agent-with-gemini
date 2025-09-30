import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types # Import types if needed for advanced usage

def main():

    load_dotenv()  # Load environment variables from a .env file if present
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    # Ensure a prompt is provided on the command line
    if len(sys.argv) < 2:
        print("i need a prompt")
    verpose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verpose":
        print("i need a prompt")
        verpose_flag = True
        sys.exit(1)
    # prompt = sys.argv[1]
    

    # Get the prompt from the command line arguments or use a default value if none is provided
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Hello, world!"
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]


    response = client.models.generate_content(
        ##free tier model
        model='gemini-2.0-flash-001', 
        contents='Why is the sky blue?'
    )
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
    if verpose_flag:
        print(f"Response Text: {response.text}")
        print(f"Usage Metadata: {response.usage_metadata}")
        print(f"Full Response: {response.userage_metadata.prompt_tokens}, {response.usage_metadata.completion_tokens}, {response.usage_metadata.total_tokens}")
        print(response.usage_metadata)

if __name__ == "__main__":
    main()