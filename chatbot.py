def welcome():
    return "welcome"
def bye():
    return "bye"
def chat():
    return "How can I assist you?"
def weather():
    return "Pleasant weather"
def default_response():
    return "This is a default message"

def chatbot():
    responses={
        "hello":welcome,
        "hi":welcome,
        "bye":bye,
        "weather":weather,
        "chat":chat
    }
    
    while True:
        user_input=input("User:").lower()
        response=responses.get(user_input,default_response)
        print("ChatBot:"+response())
        if user_input=="bye":
            break
chatbot()