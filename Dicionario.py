dicionario = {
    "Planetas": ["Terra", "Marte", "Saturno", "Mercurio", "Jupiter", "Urano", "Netuno", "Venus"],
    "Satelites": ["Lua", "Europa", "Ganymede", "Io", "Callisto", "Amalthea", "Himalia", "Adrastea"],
}

for tag in dicionario:
    print(tag)
    
for tag in dicionario:
    for planeta in dicionario["Planetas"]:
        print(planeta)
    
for tag in dicionario:
    for planetaSatelite in dicionario[tag]:
        print(planetaSatelite)