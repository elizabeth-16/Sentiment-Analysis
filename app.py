import streamlit as st
import sklearn
import joblib
model = joblib.load('Yelp_model')
st.title('Yelp Classifier')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]
