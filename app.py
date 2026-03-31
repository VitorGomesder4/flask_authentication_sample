from flask import Flask, request, jsonify, render_template
from models.user import User
from database import db

app = Flask(__name__) #instanciando flask
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app) #Iniciando db com aplicação flask
#Session <- conexão ativa

@app.route("/Ola", methods=['GET'])
def ola():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True) 