import os
import sys
from ast import Raise
from cmd import PROMPT

from dotenv import load_dotenv

from functions.call_function import available_functions
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types


def main():
    print("Hello from ai-agent!")

    verbose = False
    prompt_args = []

    for arg in sys.argv[1:]:
        if arg == "--verbose":
            verbose = True
        else:
            prompt_args.append(arg)

    if len(prompt_args) > 0:
        user_prompt = " ".join(prompt_args)
    else:
        print("Error: no prompt given")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if response.usage_metadata == None:
        raise RuntimeError("failed API request")

    x = response.usage_metadata.prompt_token_count
    y = response.usage_metadata.candidates_token_count

    if verbose == True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {x}")
        print(f"Response tokens: {y}")
        print("Response:")
        print(response.text)

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return

    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")


if __name__ == "__main__":
    main()
