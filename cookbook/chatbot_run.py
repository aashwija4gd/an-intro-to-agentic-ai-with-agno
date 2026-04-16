from agents.chatbot import chatbot

def run_chatbot_workflow():
    response = chatbot.run(
        input="Hi! I'm Aashwija. What is your name?"
    )
    print(response.content)

    response = chatbot.run(input="Do you know the meaning of my name?")
    print(response.content)

    response = chatbot.run(input="You are not helping me at all. This is stupd.")
    print(response.content)

run_chatbot_workflow()