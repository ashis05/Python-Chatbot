import nltk
from nltk.chat.util import Chat, reflections   

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"],
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking! How about you?"],
    ],
    [
        r"(.*) your name ?",
        ["I'm just a simple chatbot.",]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions and engage in conversation.",]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye!", "Bye, take care!"]
    ],
    [
        r"(.*)",
           [ "I'm Sorry I did not get that, could you rephrase it"] 
    ]
]

def simple_chatbot():
    print("Hi! I'm a simple chatbot. How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Call the function to start the chatbot
if __name__ == "__main__":
    simple_chatbot()
