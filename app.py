@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def criar_usuarios():
    novo = request.json
    novo ['id'] = len(usuarios) + 1
    usuarios.append(novo)
    return jsonify(novo), 201

if name == '__main__':
    app.run(debug=True)