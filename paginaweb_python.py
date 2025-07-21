from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def mostra_hostname():
    nome_host = socket.gethostname()
    return f"<h1>Nome host: {nome_host}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

