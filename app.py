from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def inicio():

    return "API FUNFO"

app.run(debug=True)