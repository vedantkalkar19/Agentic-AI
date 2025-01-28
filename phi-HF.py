from phi.agent import Agent
from phi.model.huggingface import HuggingFaceChat

def main():
    # Initialize the agent with Llama 3
    agent = Agent(
        model=HuggingFaceChat(
            id="meta-llama/Meta-Llama-3-8B-Instruct",
            max_tokens=4096,
        ),
        markdown=True
    )

    print("\nChatbot: Hello! I'm your Llama-powered assistant. Type 'exit' to end our chat.\n")

    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        
        # Get and display response
        print("\nChatbot:", end=" ")
        agent.print_response(user_input)
        print()  # Add empty line between exchanges

if __name__ == "__main__":
    main()