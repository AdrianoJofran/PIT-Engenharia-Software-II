from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Sistema de Controle de Manutenção Industrial"

if __name__ == "__main__":
    app.run(debug=True)
