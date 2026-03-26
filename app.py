from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "Carol"}
]

@app.route("/")
def home():
    return "API Flask rodando!"

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def criar_alunos():
    novo = request.json
    novo['id'] = len(alunos) + 1
    alunos.append(novo)
    return jsonify(novo), 201


if __name__ == "__main__":
    app.run(debug=True)