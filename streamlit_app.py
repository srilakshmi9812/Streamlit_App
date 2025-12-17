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



with st.sidebar:
  st.header("Input Features")
  island = st.selectbox("Island", ['Biscoe', 'Dream', 'Torgersen'])
  gender = st.selectbox("Gender", ['male', 'female'])
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('body mass (g)', 2600.0, 6300.0, 4207.0)

  #Create Dataframe for input features
  
  data = {'island': island, 
          'bill_length_mm': bill_length_mm, 
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis = 0)
  input_df

with st.expander('Input Features'):
  st.write('**Input Penguin Data**')
  input_df
  st.write('**Input Penguin Data Combined with Original Data**')
  input_penguins

  
#Data Preparation:  
#Encode X

encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
df_penguins
# Encode Y
target_mapper = {'Adelie' : 0, 'Chinstrap': 1, 'Gentoo': 3}
def target_encode(val):
  return target_mapper[val]
y_encode = Y.apply(target_encode)

with st.expander('Data Preparation'):
  st.write('**Encoded X (Input Penguin)**')
  df_penguins
  st.write('**Encoded Y**')
  y_encode
  


  

                  
                        
  

