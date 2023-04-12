#importando o flask para podermos usar no nosso programa
from flask import Flask

#Vamos criar uma variável (neste caso,um objeto) para representar nossa aplicacao web
app = Flask(__name__)   

#vamos criar uma rota para acessar o servidor
@app.route("/")
#ao acessar essa rota, a funçao abaixo é executada e ela devolve (return) o texto "deu certo!"
def exibir_mensagem():
 return "Deu Certo!"

#A linha abaixo executa a aplicação web que foi criada a partir do flask
app.run(debug=True)