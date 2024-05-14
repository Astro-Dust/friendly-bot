import nltk
from nltk.chat.util import Chat, reflections

# pacotes necessarios para o nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

pairs = [
  ['Hello', ['Hello! How was your day?']],
  ['(.*?)sad(.*?)', ['That is unfortunate... Can i help somehow?']],
  ['(.*?)ok(.*?)', ['It is alright, you got through one more day. Be proud of yourself.']],
  ['(.*?)great(.*?)', ['Glad to know! Keep having a great one!']],
]

# criando o chatbot
chatbot = Chat(pairs, reflections)

def talk():
  print('Welcome to Chatbot! Type "exit" to well... exit.')

  while True:
    user_input = input('You: ')
    
    if user_input.lower() == 'exit':
      print('We are done for now. Have a good day!')
      break

    chat_response = chatbot.respond(user_input)
    print('Chatbot: ', chat_response)

if __name__ == '__main__':
  talk()