""" This module contains the Flask app that serves the model. """

from flask import Flask, request, Response
from model_service.model_wrapper import ModelService

app = Flask(__name__)

model = ModelService()


@app.route("/")
def home():
    """
    This function handles the root endpoint of the Flask app.
    It returns a message indicating that the user has reached the endpoint for
        the model-service of REMLA group 8.
    """
    return "<p><b>You have reached the endpoint for the model-service of REMLA\
            group 8.</b> <br/><br/>Make a POST request to /predict with a \
            JSON with 'url': ['google.com', 'tudelft.nl'] \
            or 'url': 'google.com'.</p>"


@app.route("/predict", methods=["POST"])
def get_prediction():
    """
    This function handles the /predict endpoint of the Flask app.
    It accepts a POST request with a JSON payload containing a 'url' key.
    It uses the model to make a prediction based on the provided URL and
        returns the prediction as a JSON response.
    """
    url = request.get_json()["url"]
    prediction = model.predict(url).flatten()

    data = {"score": prediction.tolist()}
    print(data)
    return data


@app.route("/ready", methods=["GET"])
def is_ready():
    """
    This function handles the /ready endpoint of the Flask app.
    It returns a 200 status response to indicate that the app is ready.
    """
    return Response(status=200)
