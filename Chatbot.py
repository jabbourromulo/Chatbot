import json
import sys
import os
import subprocess as sp

class Joquinha():
    # construtor
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write(
                            '''
                                [   ["Joquinha"],
                                       {
                                           "oi": "Olá! Qual seu nome?",
                                           "tchau": "Tchau! Tchau!",
                                           "/lista": "O que você gostaria de adicionar na sua lista?",
                                           "/matematica": "Que conta você quer fazer?",
                                           "/contato": "Que telefone você gostaria de obter?",
                                           "/dicionario": "Digite o nome da sua lista" 
                                       },
                                    [],
                                    {
                                        
                                    }
                                ]
                            '''
                        )
            memory.close()
            memory = open(name + '.json', 'r')

        self.name = name
        self.known, self.phrases, self.lista, self.dicionario = json.load(memory)
        memory.close()
        self.historic = [None]
    
    def listen(self, phrase=None):
        return phrase.lower()

    def think(self, phrase):
        def execute(phrase):
            platform = sys.platform
            link = phrase.replace('/executa ', '')
            if 'win' in platform:
                os.startfile(link)
            if 'linux' in platform:
                try:
                    sp.Popen(link)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', link])
        
        if phrase in self.phrases:
            return self.phrases[phrase]
        # harcoded
        if phrase == '/aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == '/pesquisa':
            return "www.google.com"
        #if phrase == 'executa':
        #    return execute()
        if '/executa ' in phrase:
            execute(phrase)
            return "Ta aí meu!!"
            #/executa www.cnbc.com
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response

        if lastPhrase == 'O que você gostaria de adicionar na sua lista?':
            response = phrase.split(", ")
            self.lista.append(response)
            self.saveMemory()
            return f"Você adicionou os itens {response} na lista"

        if lastPhrase == "Digite o nome da sua lista":
            self.nomeLista = phrase
            return "O que você gostaria de adicionar na sua Lista?"

        if lastPhrase == 'O que você gostaria de adicionar na sua Lista?':
            self.dicionario[self.nomeLista] = phrase.split(", ")

            self.saveMemory()
            return f"Você adicionou os itens {phrase} na lista {self.nomeLista}"

        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'

        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'

        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'

    def getName(self, name):
        if 'Meu nome é ' in name:
            name = name[11:]
        name = name.title()
        return name
    
    def answerName(self, name):
        if name in self.known:
            if name != 'Joquinha':
                phrase = 'Eaew, '
            else:
                phrase = 'E aí chará, '
        else:
            phrase = 'Muito prazer, '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'
    
    def saveMemory(self):
        memory = open(self.name + '.json', 'w', encoding ='utf8')
        json.dump([self.known, self.phrases, self.lista, self.dicionario], memory, indent=2)
        memory.close()
                    
    def speak(self, phrase):
       # print(phrase)
        self.historic.append(phrase)