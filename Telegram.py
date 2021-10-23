import json, telepot, time
from os import name
from telepot.loop import MessageLoop
from Chatbot import Joquinha

with open("Token.json") as jsonToken:
    token = json.load(jsonToken)

telegram = telepot.Bot(token)
bot = Joquinha("Joquinha")

def receiveMessage(msg):
    frase = bot.listen(phrase=msg["text"])
    resposta = bot.think(frase)

    bot.speak(resposta)
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    telegram.sendMessage(chat_id, resposta)
    #if content_type == 'text':
        ##telegram.sendMessage(chat_id, msg['text'])
        #telegram.sendMessage(chat_id, "E ai?")

MessageLoop(telegram, receiveMessage).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)