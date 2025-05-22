import streamlit as st
import pickle

st.title("This is my web application for cal_housing")

model=pickle.load(open('rf_model_class_2_nn.pkl','rb'))


data={'MedInc':[4.5,9,6,6.5,11.6],
      'HouseAge':[5,8,15,21,30],
      'AveRooms':[5,8,6.8,7.6,11.7],
      'AveBedrms':[3,4,4,3.5,6],
      'Population':[5000,6000,8000,600,9500],
      'AveOccup':[2,5,7,11,4],
       'Latitude':[33.4,35.5,33.8,39.4,40.1],
       'Longitude':[-120.1,-119.2,-115.33, -118,-114]}


MedINCst.