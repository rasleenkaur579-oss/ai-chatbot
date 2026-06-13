responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm fine!",
    "bye": "Goodbye!"
}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(user, "I don't understand."))