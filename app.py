import streamlit as st
import pycaret
import joblib
import pandas as pd
from pycaret.regression import *

st.title("Predict Tv's Price")

support_is = st.number_input("put number of support",min_value=1)
brand = st.selectbox("Choose the Brand",['Samsung', 'TCL', 'MI', 'LG', 'OnePlus', 'Redmi', 'VU',
       'AmazonBasics', 'EAirtec', 'Sony', 'IFFALCON', 'Hisense', 'Onida',
       'Kodak',
       'Game mode, Smart Monitor, Flicker-Free, HDMI,Bluetooth, wifi connectivity',
       'Sanyo', 'AKAI', 'TOSHIBA', 'ADSUN', 'Kevin', 'Shinco', '4K'])
resolution = st.selectbox("Choose the resolution",['4K', '720p', '1080p', 'HD Ready', '2', '60 Hz'])
connectors = st.number_input("put number of connectors",min_value=1)
size = st.number_input("put size/inches",min_value=30.0)
caracts = st.selectbox("put the caracteristics",[' HDR10+', ' A+', ' LED', ' HDR 10', ' HDR10+ | HLG',
       ' Self-LIT Pixel', ' IPS', ' Bezel-less Design', '', ' A+ Grade',
       ' HDR10+ | HDR10 | HLG', ' Slim Design', '60 Hz',
       ' Quantum HDR + HDR 10+', ' OLED'])

c = st.beta_columns(10)
pred = c[5].button("predict")

df_test = pd.DataFrame([[support_is,brand,connectors,resolution,size,caracts]],columns=["supported internet service","Brand","connector","resolution","size_inch","caracteristiques"])


oe = joblib.load("./oe.pkl")
df_test[["Brand","resolution","caracteristiques"]] = oe.transform(df_test[["Brand","resolution","caracteristiques"]])

model = load_model("./rf")
prediction = predict_model(model,df_test)
if pred:
       c = st.beta_columns(10)
       st.balloons()
       c[5].success(prediction["Label"][0])