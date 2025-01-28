import os
os.environ["GRPC_VERBOSITY"] = "ERROR"

import google.generativeai as genai

genai.configure(api_key="API key")

# Create the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 65536,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

print("\nWelcome to Gemini Chat! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['exit', 'quit']:
        print("Gemini: Goodbye! 👋")
        break
    
    # Add line after input
    print("-" * 25)
    
    try:
        response = chat_session.send_message(user_input)
        # Add line before and after response
        print(f"\nGemini: {response.text}\n")
        print("-" * 25)
    except Exception as e:
        print(f"\nError: {str(e)}\n")
        print("-" * 25)
