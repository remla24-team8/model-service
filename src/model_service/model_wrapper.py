"""
This module contains the ModelService class, which is responsible for loading the model
and making predictions.
"""

import os
import gdown
from keras.models import load_model
from lib_ml.process_data import DataProcessor


class ModelService:
    """
    A class that represents a model service for loading the model and making predictions.
    """

    def __init__(self):
        self.model = self.get_model()
        self.processor = DataProcessor(
            tokenizer_url="https://drive.google.com/drive/u/0/folders/1Z0bbPcIegbLHjJcZ90CqzVPmCBLlYEkj"
        )

    def predict(self, url):
        """
        Make a prediction using the stored model and a given url as input.

        Args:
            url (str or list): The URL(s) to be used for prediction.

        Returns:
            numpy.ndarray: The predicted values.
        """
        if isinstance(url, list):
            data = url
        else:
            data = [url]
        preprocess_url = self.processor.tokenize_pad_data(data)
        prediction = self.model.predict(preprocess_url, verbose=0)

        return prediction

    @staticmethod
    def get_model():
        """
        Load the model from the local file system or download it if necessary.

        Returns:
            keras.models.Model: The loaded model.
        """
        if os.path.exists("models/model.h5"):
            model = load_model("models/model.h5", compile=True)
            return model

        if not os.path.exists("models/"):
            os.makedirs("models/")

        gdrive_url = "https://drive.google.com/drive/u/0/folders/1ITlzN-9Qe7ZnNRGWkq-YHrjt9xYG3e_-"
        model_out = "./"
        gdown.download_folder(gdrive_url, output=model_out)
        model = load_model("models/model.h5", compile=True)
        return model
