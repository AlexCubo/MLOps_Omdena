"""Flask app to predict daily global horizontal irradiance (daily_GHI)
of Sassari City (Italy). The data are taken from Solcast time series.
This project is part of MLOps Omdena course, December 2021.
I would like to thank Solcast, Omdena, Joseph Itopa (the teacher)"""

'''Inputs:
{
    "month": <val>,
    "year": <val>,
    "daily_temp": <val>,
    "daily_rain": <val>,
    "daily_hum": <val>,
    "daily_press": <val>,
    "daily_windDir": <val>,
    "daily_windSp": <val>,
    "daily_DHI": <val>,
    "daily_DNI": <val>
}

Output:
{
    "daily_GHI": <val>
}
'''
# import modules
import pandas as pd
from flask import Flask, jsonify, request
import numpy as np
import joblib

print("Welcome to flask app!")
# instantiate flask object
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def get_input():
    ''' A flask app to interact with ML model and user request'''
    # load packets
    packet = request.get_json(force=True)
    # transform packet in DataFrame
    # (is needed because I used ColumnTransformer in my ML)
    data_df = pd.DataFrame(packet, index=[0])
    #load model
    filename = 'app/models/gbr_model.pkl'
    loaded_model = joblib.load(filename)
    # prediction
    predicted_GHI = loaded_model.predict(data_df)[0]

    return jsonify(packet, {"daily_GHI": predicted_GHI})
    #return "A Heroku message"


'''
filename = './models/gbr_model.pkl'
loaded_model = joblib.load(filename)
data_dir = {
"month":8,
"year":2020,
"daily_temp":28.3,
"daily_rain":38.1,
"daily_hum":72.4,
"daily_press":991.0,
"daily_windDir":140.3,
"daily_windSp":3.8,
"daily_DHI":152.5,
"daily_DNI":203.7
}
print(type(data_dir))
data_df = pd.DataFrame(data_dir, index=[0])
print(data_df)
#



predicted_GHI = loaded_model.predict(data_df)
print(predicted_GHI)
'''
