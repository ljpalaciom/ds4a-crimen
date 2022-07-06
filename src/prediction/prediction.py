import glob
import joblib
import numpy as np
from os.path import basename
from datetime import datetime, timedelta
from dao.dao_sql import crimes_amount_last_day

class PredictionModelArima:

    def __init__(self):
        self.models_paths = {basename(path).split("-")[0]:path for path in glob.glob("prediction/trained_models_arima/*.pkl")}

    def _load_model(self, model):
        try:
            return joblib.load(self.models_paths[model])
        except KeyError as e:
            raise Exception(f"Model {model} is not available. Exception: {e}")

    def predict(self, locality_code, start_date, end_date):
        if locality_code == "all":
            last_value = crimes_amount_last_day()
        else:
            raise Exception(f"locality_code {locality_code} not supported in the moment")
        return np.exp(self._load_model(locality_code).predict(start_date + timedelta(days=1), end_date).cumsum().fillna(0))*last_value

class PredictionModelLSTM:
    def __init__(self):
        self.scaler_paths = {basename(path).split("-")[0]:path for path in glob.glob("prediction/trained_models_lstm/*scaler*.pkl")}
        self.models_paths = {basename(path).split("-")[0]:path for path in glob.glob("prediction/trained_models_lstm/*.h5")}

    def _load_scaler(self, scaler):
        try:
            return joblib.load(self.scaler_paths[scaler])
        except KeyError as e:
            raise Exception(f"Scaler {scaler} is not available. Exception: {e}")
    
    def _load_model(self, model):
        from keras.models import load_model
        try:
            return load_model(self.models_paths[model])
        except KeyError as e:
            raise Exception(f"Model {model} is not available. Exception: {e}")
    
    def predict(self, locality_code, start_date, end_date):
        if locality_code == "all":
            scaler = self._load_scaler(locality_code)
            model = self._load_model(locality_code)
        else:
            raise Exception(f"Locality code {locality_code} not supported in the moment")
       