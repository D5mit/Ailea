from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot
ailea = ChatBot(
    'Ailea',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am spesifically trainined to help with the AIAF.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database-chatbot.db'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(ailea)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

conversation = [
    "What is an AIAF?",
    "It is an artificial intelligence adoption framework."
]
trainer = ListTrainer(ailea)
trainer.train(conversation)

print('Type something to begin...')

if __name__ == '__main__':
    # The following loop will execute each time the user enters input
    icontinue = True
    while True:
        try:
            user_input = input()
            print(user_input)
            if user_input == 'exit':
                icontinue = False
            else:
                bot_response = ailea.get_response(user_input)
                print(bot_response)


        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break



