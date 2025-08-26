import streamlit as st
import pickle
st.title('Weather Predictor')
preci=st.number_input('Enter the precipitation')
temp_max=st.number_input('Enter the maximum temperature')
temp_min=st.number_input('Enter the minimum temperature')
wind=st.number_input('Enter the wind speed')
button=st.button('Predict')
if button:
        if preci >= 0 and temp_max >= 0 and temp_min >= 0 and wind >= 0:
            model=pickle.load(open('wp.pkl','rb'))
            res=model.predict([[preci,temp_max,temp_min,wind]])
            st.subheader(f'Weather Prediction : {res}')
        else:
            st.subheader('Please enter valid values for precipitation, temperature, and wind speed.')