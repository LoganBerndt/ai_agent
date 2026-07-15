import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import call_function, available_functions


# Main function - This is the entry point of the application. It initializes the OpenAI client, sets up the command-line argument parser, 
# and manages the interaction loop with the AI agent. The loop continues until a response is received without any tool calls or until a 
# maximum number of iterations is reached. The function also handles verbose output for debugging purposes.
def main():

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("API Key not found.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {
            "role": "system", 
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]

    for task in range(20):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )  


        check_usage = response.usage
        
        if args.verbose == True:
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {completion_tokens}")
            print(f"User prompt: {args.user_prompt}")
            
        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)

                if len(result_message['content']) == 0:
                    raise Exception("Content is empty")
                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            print(message.content)
            break
    else:    
        print("Error: Maximum iteration range reached. Terminating process.")
        exit(1)




if __name__ == "__main__":
    main()