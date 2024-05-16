from flask import Flask, request
from model_service.model_wrapper import ModelService

app = Flask(__name__)

model = ModelService()

@app.route("/")
def home():
    return "<p>You have reached the endpoint for the model-service of REMLA group 8. \nMake a POST request to /predict with a JSON with 'url': data.</p>"

@app.route("/predict", methods=["POST"])
def get_prediction():
    url = request.get_json()["url"]
    prediction = model.predict(url)
    print({
        "prediction": list(prediction)
    })

    return {
        "prediction": list(prediction)
    }
