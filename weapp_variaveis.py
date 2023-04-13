#vamos criar um dicionario com duas chaves e entar retornar seus dados pela rota
dicionario = {
    "nome": "Eduardo Domingues",
    "nascimento": 1989
}

#importar flask
from flask import Flask
#criando a aplicacao Flask
app = Flask(__name__)

#a rota abaixo aciona uma funcao que retorna um dicionario
@app.route("/teste")
def mostra_dicionario():
    return "teste_2"

@app.route("/")
def dados_usuario():
    return f"O usuario {dicionario['nome']} nasceu em {dicionario['nascimento']}"

#colocar a aplicacao para rodar
app.run(debug=True)
