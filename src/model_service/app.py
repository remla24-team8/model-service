from flask import Flask, request
import gdown
import os
from keras.models import load_model
from lib_ml.process_data import DataProcessor

app = Flask(__name__)


class ModelService:
    
    def __init__(self):
        self.model = self.get_model()
        self.processor = DataProcessor()



    @staticmethod    
    def get_model():
        if os.path.exists("models/model.h5"):
            model = load_model("models/model.h5", compile=True)
            return model
        
        gdrive_url = "https://drive.google.com/drive/folders/1io5_6ifcMol1M9jwZNw9BvRt7X9psTuc"
        model_out = "models/model.h5"
        model_name = gdown.download(gdrive_url, model_out, fuzzy=True)
        model = load_model(model_name, compile=True)
        return model




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