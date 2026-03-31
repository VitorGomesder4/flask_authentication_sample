from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route("/Ola", methods=['GET'])
def ola():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True) 