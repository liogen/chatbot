from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

"""
This example shows how to create a chat bot that
will learn responses based on an additional feedback
element from the user.
"""

# Uncomment the following line to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Feedback Learning Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
    #     'chatterbot.logic.BestMatch',
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.UnitConversion',
    # ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    'chatterbot.corpus.english'
)

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
