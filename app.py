import pandas as pd
import numpy as np
import streamlit as st
import pickle

#Load all the instances that are required

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

def prediction(input_data):
   scaled_data = scaler.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]
    

    if pred==0:
      return 'Developed'
    elif pred==1:
      return 'Developing'
    else:
      return 'Under Developed'
def main():
  st.title("HELP International Foundation")
  st.subheader("A machine learning model to predict a country's socio-economic and health factors")
  chld_mor=st.text_input("Enter child mortality rate")
  lf_exp=st.text_input("Enter Life expectancy")
  tot_fert=st.text_input("Enter Total fertility rate")
  health=st.text_input("Enter % of GDP spent on Health")
  exports=st.text_input("Enter % of GDP spent on Exports")
  imports=st.text_input("Enter % of GDP spent on Imports")
  gdp=st.text_input("Enter GDP per population")
  income=st.text_input("Enter Income per person") 
  infl=st.text_input("Enter Inflation rate")
  
  inp_list=[[chld_mor, lf_exp, tot_fert, health, exports, imports, gdp, income, inf]]

  if st.button("Predict"):
    response=prediction(inp_list)
    st.success(response)

if __name__ == '__main__':
    main()
