'''
Solar radiation app to be used with streamlit.
Thanks to Sandra Boniface to make me discover the wonderful world of streamlit.
'''

# import main libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path

# import serializer
import pickle

# import streamlit
# att! to import successfully streamlit you need 7.0 < click < 8.0
import streamlit as st

lr_model_path = "../bin/models/lr_model.pkl"
rf_model_path = "../bin/models/rf_model.pkl"
gbr_model_path = "../bin/models/gbr_model.pkl"

months_list = ['January', 'February', 'March', 'April',
               'May', 'June','July', 'August',
               'September', 'October', 'November', 'December']

years_list = [2019, 2020, 2021]

st.write("""
         # Solar Radiation Predictor

         This application was developed during the Omdena course
         "MLOps for AI Engineers and Data Scientists" in December 2021.

         The application predicts the global horizontal irradiance (GHI) in the
         city of Sassari (Italy) by using 3 different ML algorithms:  \n
            1. Linear Regressor
            2. Random Forest Regressor
            3. Gradient Boosting Regressor \n
         The training data are historical data taken from
         [Solcast](https://solcast.com/) \n

         The author would like to thank Omdena and teacher Joseph Itopa.
         """)

st.write("---")

st.header('Models')
selected_model = st.radio('Choose the model you want to use',
                          ['Linear Regressor',
                           'Random Forest Regressor',
                           'Gradient Boosting Regressor'])

if selected_model == 'Linear Regressor':
    loaded_model = pickle.load(open(lr_model_path, 'rb'))
elif selected_model == 'Random Forest Regressor':
    loaded_model = pickle.load(open(rf_model_path, 'rb'))
elif selected_model == 'Gradient Boosting Regressor':
    loaded_model = pickle.load(open(gbr_model_path, 'rb'))

st.write("---")

st.header('Inputs')

col1, col2 = st.columns(2)

month = col1.selectbox('Month', months_list)

year = col2.selectbox('Year', years_list)

c1, c2, c3, c4 = st.columns(4)
daily_temp = c1.number_input('Average daily temperature (Celsius)',
                             min_value = -10.0,
                             max_value = 50.0,
                             value = 20.0)

daily_rain = c2.number_input('Average daily precipitaion (mm)',
                             min_value = 4.0,
                             max_value = 40.0,
                             value = 20.0)

daily_hum = c3.number_input('Average daily humidity .... (%)',
                             min_value = 0.0,
                             max_value = 100.0,
                             value = 50.0)

daily_press = c4.number_input('Average daily pressure (mbar)',
                             min_value = 950.0,
                             max_value = 1030.0,
                             value = 990.0)
daily_windDir = c1.number_input('Average daily wind direction (Degrees)',
                             min_value = 0.0,
                             max_value = 360.0,
                             value = 180.0)

daily_windSp = c2.number_input('Average daily wind speed (m/s)',
                             min_value = 0.0,
                             max_value = 30.0,
                             value = 10.0)

daily_DHI = c3.number_input('Average daily DHI (Diffuse Horizontal Irradiance)',
                             min_value = 0.0,
                             max_value = 350.0,
                             value = 150.0)

daily_DNI = c4.number_input('Average daily DNI (Direct Normal Irradiance)',
                             min_value = 0.0,
                             max_value = 800.0,
                             value = 350.0)


st.write('---')

# Transform selected input data into a dataframe
features = {
    'month': months_list.index(month)+1,
    'year' : year,
    'daily_temp': daily_temp,
    'daily_rain': daily_rain,
    'daily_hum': daily_hum,
    'daily_press': daily_press,
    'daily_windDir': daily_windDir,
    'daily_windSp': daily_windSp,
    'daily_DHI': daily_DHI,
    'daily_DNI': daily_DNI
}

features_df = pd.DataFrame([features])

# display given input in a table
st.header("Given Inputs")
st.table(features_df)

# Return prediciton
st.header('Results')

if st.button('Predict'):
    prediction = loaded_model.predict(features_df)
    st.write(f'Global Horizontal Irradiance is {round(prediction[0], 2)}')
    st.write(f"Calculation perfomed using the ***{selected_model}*** algorithm.")

st.write('---')

st.markdown(
    "**Rendering and algorithms by Alessandro Cubeddu**"
    )
st.markdown(
    "**Contact: alessandro.cubeddu@yahoo.co.uk**"
    )


