from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Brandon',
              trainer='chatterbot.trainers.ListTrainer')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing",
    "I'm doing great, how about you",
    "That is good to hear",
    "Thank you",
    "You're welcome"
])

trainer.train([
    "Good bye!",
    "See you soon!"
])

response = chatbot.get_response("Thank you")

print(response)