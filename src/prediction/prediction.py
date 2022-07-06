import glob
import joblib
import numpy as np
from os.path import basename
from datetime import datetime, timedelta
import pandas as pd
from dao.dao_sql import crimes_amount_last_day, crimes_over_time_day_data

class PredictionModelArima:

    def __init__(self):
        self.models_paths = {basename(path).split("-")[0]:path for path in glob.glob("prediction/trained_models_arima/*.pkl")}

    def _load_model(self, model):
        try:
            return joblib.load(self.models_paths[model])
        except KeyError as e:
            raise Exception(f"Model {model} is not available. Exception: {e}")

    def predict(self, locality_code, max_date_data, end_date):
        if locality_code == "all":
            last_value = crimes_amount_last_day()
        else:
            raise Exception(f"locality_code {locality_code} not supported in the moment")
        predictions = np.exp(self._load_model(locality_code).predict(max_date_data + timedelta(days=1), end_date).cumsum().fillna(0))*last_value
        return predictions.reset_index().rename(columns={"index":"fecha", 0: "crimes"})

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
    
    def predict(self, locality_code, max_date_data, end_date):
        if locality_code == "all":
            scaler = self._load_scaler(locality_code)
            model = self._load_model(locality_code)
            n_steps_input = model.layers[0].input_shape[1]
            crimes_by_day = crimes_over_time_day_data(max_date_data - timedelta(days=n_steps_input -1), max_date_data)
            scaled_data = scaler.transform(crimes_by_day["crime amount"].values.reshape(-1,1))
            prediction = model.predict(scaled_data.reshape(1, n_steps_input, 1))
            prediction = scaler.inverse_transform(prediction).reshape(-1)
            days_to_predict = abs((end_date - max_date_data).days)
            return pd.DataFrame({"crimes": prediction[:days_to_predict], "fecha": pd.date_range(max_date_data + timedelta(days=1), end_date)})  
        else:
            raise Exception(f"Locality code {locality_code} not supported in the moment")
       