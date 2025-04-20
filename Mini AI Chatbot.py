## MINI AI CHATBOT 
## BY HARSH P. S. PARIHAR 

import random

def chatbot():
    print("Hello! I'm MiniBot. Type 'bye' to exit.")

    responses = {
        "hi": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thank you!", "Doing great! How about you?", "I'm here to help you!"],
        "what is your name": ["I'm MiniBot!", "They call me MiniBot.", "Just a little bot here to chat!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting! Tell me more."]
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("MiniBot: " + random.choice(responses["bye"]))
            break

        matched = False
        for key in responses:
            if key in user_input:
                print("MiniBot: " + random.choice(responses[key]))
                matched = True
                break

        if not matched:
            print("MiniBot: " + random.choice(responses["default"]))

chatbot()
