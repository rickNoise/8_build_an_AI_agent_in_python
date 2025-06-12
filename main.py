import os, sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print("\nUsage: python main.py 'your prompt here'")
        print("Example: python main.py 'How do I build a calculator app?'")
        sys.exit(1)
    user_prompt = " ".join(args)

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
