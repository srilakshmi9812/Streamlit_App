import streamlit as st
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt


st.title('Machine Learning App')

st.info("This app builds Machine Learning Model")

with st.expander("Data"):
  st.write("**Raw Data**")
  data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  data
  
  st.write("### **Input Features**")
  X= data.drop("species", axis = 1)
  X
  
  st.write("### **Output, Y**")
  Y = data.species
  Y
  
with st.expander("Data Visualization"):
  st.scatter_chart(data=data, x="bill_length_mm", y="body_mass_g", color = 'species')

#Data Preparation:

with st.sidebar:
  st.header("Input Features")
  island = st.selectbox("Island", ['Biscoe', 'Dream', 'Torgersen'])
  gender = st.selectbox("Gender", ['male', 'female'])
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('body mass (g)', 2600.0, 6300.0, 4207.0)

                  
                        
  

