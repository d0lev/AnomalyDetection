import streamlit as st
import sklearn as sk
import pandas as pd
import joblib
import numpy as np
from PIL import Image

IsolationForest = open("model\classifier.pkl","rb")
classifier = joblib.load(IsolationForest)


def predict_anomaly(data):
  result = classifier.predict(np.array(data).reshape(1,-1))
  return result[0]



if __name__ == "__main__":
  html_temp = """
  <div style= "background-color:#F1F9FF; padding: 35px;width: 110%;   font-family:JetBrainsMono;">
  <h2 style = "font-family:JetBrainsMono; color:#058aff; text-align: center;"> Anomaly Detection </h2>
  <p style = "text-align: center; font-family:JetBrainsMono; color:grey; ">This project was taken as part of the course: Methods for detecting cyber attacks by Dr. Ran Dubin from Ariel University.</p>
  <p style = "font-size: 3; font-family:JetBrainsMono; text-align: left;"> Dolev Abuhazira
        <a href="mailto:dolevictory@gmail.com">Send Email </a>
        </p>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  features = [1] #put dummy variable for the record id feature

  duration_header = """ <h1 style = "font-size: 15px; font-family:JetBrainsMono; margin-bottom:-50px" >number of seconds (rounded) of the connection</h1> """
  source_bytes_header = """ <h1 style = "font-size: 15px; font-family:JetBrainsMono; margin-bottom:-50px" >number of data bytes transferred from the source to the destination</h1> """
  destination_bytes_header = """ <h1 style = "font-size: 15px; font-family:JetBrainsMono; margin-bottom:-50px" >number of data bytes transferred from the destination to the source</h1> """

  st.markdown(duration_header,unsafe_allow_html=True)
  duration = st.number_input(label = "")
  features.append(duration)

  st.markdown(source_bytes_header,unsafe_allow_html=True)
  source_bytes = st.number_input(label = " ")
  features.append(source_bytes)

  st.markdown(destination_bytes_header,unsafe_allow_html=True)
  destination_bytes = st.number_input(label = "  ")
  features.append(destination_bytes)
 
  print(features)
  m = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        height: 3em;
                        width: 10em;
                        position: relative;
                        margin-left: 300px; 
                        font-family:JetBrainsMono;
                    }
                    </style>""", unsafe_allow_html=True)

if st.button("PREDICT"):
    output = predict_anomaly(features)
    if output == -1:
          st.markdown(""" <p style = "margin-left: 160px;  font-family:JetBrainsMono; color:grey; ">The model prediction for the record is <a style = "font-weight: bold; color:#cc0000;"> Anomalous. </a></p>""",unsafe_allow_html=True)
    else:
          st.markdown(""" <p style = "margin-left: 160px;  font-family:JetBrainsMono; color:grey; ">The model prediction for the record is <a style = "font-weight: bold; color:#0080f0;"> Normal. </a></p>""",unsafe_allow_html=True)


st.markdown("""<p style = "margin-left: 170px; font-size: 3; font-family:JetBrainsMono; text-align: left;"> For more details visit my 
        <a href="https://github.com/d0lev/AnomalyDetection">github repository </a>
        </p>""",unsafe_allow_html= True)