import json

lista = []

print('Iremos cadastrar 4 usuários para criar um arquivo json.\n')

for id in range(1, 5):
    nome = input('Digite seu nome: ')
    ano = input('Ano de nascimento: ')
    dicionario = {"id":id, "nome": nome, "Data de nascimento": ano}
    lista.append(dicionario)

print(lista)


json_string = json.dumps(lista, indent=3)

# Salva o JSON em um arquivo
with open("dicionario.json", "w") as arquivo_json:
    arquivo_json.write(json_string)
