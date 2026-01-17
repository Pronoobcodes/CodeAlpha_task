responses = {
    "hello": "Hi there!",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I'm a basic python chatbot created for CodeAlpha.",
    "help": "Sure! How can I assist you?",
    
}

while True:
    print("You can ask me things like 'hello', 'how are you', 'what is your name', or say 'bye' to exit.")
    user_input = input("You: ").lower()
    if user_input in responses:
        print("Chatbot:", responses[user_input])
    else:
        print("Chatbot: I'm sorry, I don't understand that.")
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break