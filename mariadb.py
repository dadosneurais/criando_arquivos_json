import mysql.connector
import json

# Estabelece a conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhadb",
    database="nome_db"
)

# Cria um cursor para executar consultas SQL
cursor = conn.cursor()

# Executa uma consulta
cursor.execute("SELECT * FROM nome_table")

# Recupera os resultados da consulta
resultados = cursor.fetchall()

# Itera sobre os resultados e imprime cada linha
for linha in resultados:
    # print(linha) # esse código já imprime os dados, porém em tuplas ()
    id, nome, senha = linha
    print(id, nome, senha) # dessa forma é retirado das tuplas ()

# Fecha o cursor e a conexão
cursor.close()
conn.close()

########################## JSON ##########################
# Converte os resultados em uma lista de dicionários
dados_json = []
for linha in resultados:
    id, nome, senha = linha  # Supondo que a ordem das colunas seja id, nome e senha
    dados_json.append({"id": id, "nome": nome, "senha": senha})

# Converte a lista de dicionários em formato JSON
json_string = json.dumps(dados_json, indent=3) # json.dumps estou chamando a biblioteca e ident é a identação do arquivo dados.json

# Salva o JSON em um arquivo
with open("dados.json", "w") as arquivo_json:
    arquivo_json.write(json_string)


# ###### direto pelo terminal ######
# sudo mysql -h localhost -u root -p db_web -e "select * from sql_injection" > data.txt
