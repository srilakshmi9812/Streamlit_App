import streamlit as st

st.title('Machine Learning App')

data = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
data
