# -*- coding: utf-8 -*-
"""Useful Linkedin Connects.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1onyGXzQzMW8exK4rHVQ9WezidUxEAqLI
"""


import os
import pandas as pd
import streamlit as st
from useful_linkedin_connects import main_function


# Page Config
st.set_page_config(
    page_title="Contexted Linkedin App",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded",

)

# App Title
st.title("Contexted Linkedin 📷")

# Columns
col1, col2 = st.columns(2)

# Input for the query
with col1:
    st.header("Input your query")
    user_query = st.text_input('Enter your query:')

# CSV File Upload
with col2:
    st.header("Upload a CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        # Load default CSV if no file is uploaded
        df = pd.read_csv('./enriched_data_linkedin_data_connections.csv')

result = main_function(user_query=user_query, csv_file=uploaded_file)

if result:
    st.write(result)
