from flask import Flask, request, jsonify, render_template
from models.user import User
from database import db
from login import login_manager

app = Flask(__name__) #instanciando flask
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app) #Iniciando db com aplicação flask
#Session <- conexão ativa

login_manager.init_app(app)

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        pass
    
    
    return jsonify({"message": "credenciais invalidas"}), 400

@app.route("/Ola", methods=['GET'])
def ola():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True) 