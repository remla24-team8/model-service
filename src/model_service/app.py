from flask import Flask
from model_service.spam import eggs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/spam/eggs")
def spam_eggs():
    return {
        "result": eggs()
    }