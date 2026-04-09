from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
    }
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def criar_livros():
    novo = request.json
    novo['id'] = len(livros) + 1
    livros.append(novo)
    return jsonify(novo), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livros(id):
    for livro in livros:
        if livro['id'] == id:
            dados = request.json
            livro['nome'] = dados.get('nome', livro['nome'])
            return jsonify(livro)
    return {"erro": "Livro não encontrado"}, 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livros(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return {"mensagem": "Livro removido"}
    return {"erro": "Livro não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)
