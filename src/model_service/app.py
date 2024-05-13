from flask import Flask, request
from model_service.spam import eggs
import gdown

app = Flask(__name__)


def get_model():

    gdrive_url = "https://drive.google.com/drive/folders/1io5_6ifcMol1M9jwZNw9BvRt7X9psTuc"
    model_out = "models/model.h5"
    mod = gdown.download(gdrive_url, model_out, fuzzy=True)
    return mod



model = get_model()

# @app.route('/predict', methods =['POST '])
# def predict():
#     """
#     Make a prediction using the stored model and a given url as input
#     """
#     preprocess_url = request.json #Still have to apply preprocessing

#     prediction = model.predict(preprocess_url)

#     print(prediction)
#     # bin_pred = (np.array(prediction))



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/spam/eggs")
def spam_eggs():
    return {
        "result": eggs()
    }