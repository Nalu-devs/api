from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def inicio():
    return send_from_directory(app.root_path, "index.html")

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.root_path, filename)

if __name__ == '__main__':
    app.run(debug=True)
