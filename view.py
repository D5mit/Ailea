from chatterbot import ChatBot

# Create a new instance of a ChatBot
ailea = ChatBot(
    'Ailea',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database-chatbot.db'
)

print('Type something to begin...')

if __name__ == '__main__':
    # The following loop will execute each time the user enters input
    icontinue = True
    while True:
        try:
            user_input = input()

            if user_input == 'exit':
                break
                icontinue = False
            else:
                bot_response = ailea.get_response(user_input)
                print(bot_response)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


