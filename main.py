import os, sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        raise ValueError("Prompt not provided as a command line argument.")
    user_prompt = sys.argv[1]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=user_prompt
    )
    
    print(f"Response: {response.text}")
    usage_metadata = response.usage_metadata
    print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
    print(f"Response tokens: {usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
