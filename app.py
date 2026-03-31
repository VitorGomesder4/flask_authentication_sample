from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instanciando flask
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app) #instanciando Database com aplicação flask

@app.route("/Ola", methods=['GET'])
def ola():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True) 