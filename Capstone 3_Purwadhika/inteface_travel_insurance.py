import streamlit as st
import pickle
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE

# Load the pre-trained pipeline
with open('Erza_Anandhika_Capstone 3_Travel Insurance.sav', 'rb') as file:
    pipeline = pickle.load(file)

st.title('''Travel Insurance Coverage Prediction App
            By Erza Anandhika Valerian Vacquier JCDSOL - 013''')

st.markdown("""
## Predicting Travel Insurance Coverage
Use this app to predict whether a travel insurance will be get coverage based on various features.
""")

# User inputs for the features
agency = st.selectbox('Agency', ['C2B', 'EPX', 'JZI', 'CWT', 'LWC', 'ART', 'CSR', 'RAB', 'KML', 'SSI', 'TST', 'TTW', 'ADM', 'CCR', 'CBH'])
agency_type = st.selectbox('Agency type', ['Airlines', 'Travel Agency'])
distribution_channel = st.selectbox('Distribution Channel', ['Online', 'Offline'])
product_name = st.selectbox('Product Name', ['Annual Silver Plan', 'Cancellation Plan', 'Basic Plan',
       '2 way Comprehensive Plan', 'Bronze Plan',
       '1 way Comprehensive Plan', 'Rental Vehicle Excess Insurance',
       'Single Trip Travel Protect Gold', 'Silver Plan', 'Value Plan',
       '24 Protect', 'Annual Travel Protect Gold', 'Comprehensive Plan',
       'Ticket Protector', 'Travel Cruise Protect',
       'Single Trip Travel Protect Silver',
       'Individual Comprehensive Plan', 'Gold Plan', 'Annual Gold Plan',
       'Child Comprehensive Plan', 'Premier Plan',
       'Annual Travel Protect Silver',
       'Single Trip Travel Protect Platinum',
       'Annual Travel Protect Platinum',
       'Spouse or Parents Comprehensive Plan',
       'Travel Cruise Protect Family'])
duration = st.number_input('Duration', min_value=0, step=1, value=0)
net_sales = st.number_input('Net Sales', min_value=0, step=1, value=0)
commision = st.number_input('Commision', min_value=0, step=1, value=0)
age = st.number_input('Age', min_value=0, step=1, value=0)

# Create a DataFrame with the inputs
data = {
    'agency': [agency],
    'agency_type': [agency_type],
    'distribution_channel': [distribution_channel],
    'product_name': [product_name],
    'duration': [duration],
    'net_sales': [net_sales],
    'commision': [commision],
    'age': [age],
}

input_df = pd.DataFrame(data)
if st.button('Predict'):
    prediction = pipeline.predict(input_df)
    
    st.subheader('Prediction Result')
    if prediction[0] == 1:
        st.write('The travel insurance will get coverage.')
    else:
        st.write('The travel insurance will not get coverage.')

# Button to reset/flush
if st.button('Reset'):
    st.experimental_rerun()