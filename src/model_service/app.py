from flask import Flask, request, Response
from model_service.model_wrapper import ModelService

app = Flask(__name__)

model = ModelService()

@app.route("/")
def home():
    return "<p><b>You have reached the endpoint for the model-service of REMLA group 8.</b> <br/><br/>Make a POST request to /predict with a JSON with 'url': ['google.com', 'tudelft.nl'] or 'url': 'google.com'.</p>"

@app.route("/predict", methods=["POST"])
def get_prediction():
    url = request.get_json()["url"]
    prediction = model.predict(url).flatten()

    data = {"score": prediction.tolist()}
    print(data)
    return data

@app.route("/ready", methods=["GET"])
def is_ready():
    return Response(status=200)