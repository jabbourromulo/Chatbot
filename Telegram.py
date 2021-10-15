import json, telepot, time
from telepot.loop import MessageLoop

with open("Token.json") as jsonToken:
    token = json.load(jsonToken)

telegram = telepot.Bot(token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #telegram.sendMessage(chat_id, msg['text'])
        telegram.sendMessage(chat_id, "E ai?")

MessageLoop(telegram, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)