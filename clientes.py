import json

def clientes ():
    with open('clientes.json', 'r', encoding='utf-8') as file:
        clientes_data = json.load(file)
    return clientes_data
print (clientes())