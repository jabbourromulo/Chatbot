import json, Dicionario

dici = Dicionario.dicionario

with open("Espaco.json","w") as espacoJson:
    json.dump(dici, espacoJson, indent=2)

with open("Espaco.json") as espacoJson:
    espacoLeitura = json.load(espacoJson)
print(espacoLeitura)

for tag in espacoLeitura:
    print(tag) 