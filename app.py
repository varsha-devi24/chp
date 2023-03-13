import streamlit as st
import pandas as pd
import pickle
import json

# Load locality JSON file
with open('E:\CHP\model\columns.json', 'r') as f:
    localities = json.load(f)

# Create locality map
locality_map = {localities[i]: i for i in range(len(localities))}

# Load model
with open('E:\CHP\model\home_price_prediction_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Sidebar
st.sidebar.header("Chennai Home Price Prediction")
locality = st.sidebar.selectbox("Locality", sorted(localities))
area_sqft = st.sidebar.slider("Area in Square Feet", min_value=500, max_value=10000, step=100, value=1000)
bhk = st.sidebar.slider("BHK", min_value=1, max_value=5, step=1, value=1)
bathrooms = st.sidebar.slider("Number of Bathrooms", min_value=1, max_value=5, step=1, value=1)

# Prediction
locality_id = locality_map[locality]
price = model.predict([[locality_id, area_sqft, bhk, bathrooms]])[0]

# Display result
st.header("Result")
st.write(f"Estimated Price: ₹{price:.2f}")
