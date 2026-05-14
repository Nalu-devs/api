from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def inicio():

    return "API FUNFO"

app.run(debug=True)

app = Flask(__name__)

usuarios = [
   
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "zipcode": "92998-3874",
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "email": "Shanna@melissa.tv",
    "zipcode": "90566-7771",
  },
  {
    "id": 3,
    "name": "Clementine Bauch",
    "email": "Nathan@yesenia.net",
    "zipcode": "59590-4157",
  },
  {
    "id": 4,
    "name": "Patricia Lebsack",
    "email": "Julianne.OConner@kory.org",
    "zipcode": "53919-4257",
  },
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "email": "Lucio_Hettinger@annie.ca",
    "zipcode": "33263",
  },
  {
    "id": 6,
    "name": "Mrs. Dennis Schulist",
    "email": "Karley_Dach@jasper.info",
    "zipcode": "23505-1337",
  },
  {
    "id": 7,
    "name": "Kurtis Weissnat",
    "email": "Telly.Hoeger@billy.biz",
    "zipcode": "58804-1099",
  },
  {
    "id": 8,
    "name": "Nicholas Runolfsdottir V",
    "email": "Sherwood@rosamond.me",
    "zipcode": "45169",
  },
  {
    "id": 9,
    "name": "Glenna Reichert",
    "email": "Chaim_McDermott@dana.io",
    "zipcode": "76495-3109",
  },
  {
    "id": 10,
    "name": "Clementina DuBuque",
    "email": "Rey.Padberg@karina.biz",
    "zipcode": "31428-2261",
  }
]

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
