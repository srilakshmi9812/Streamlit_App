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

