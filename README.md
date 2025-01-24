# Socio-Economic-stats-and-Financial-Aid--CountryWise


https://socio-economic-stats-and-financial-aid--countrywise-r6qq3dlaar.streamlit.app
HELP International Foundation Prediction App

Project Overview

This project is a web-based application built using Streamlit. It predicts a country's socio-economic and health development status based on key indicators like child mortality, life expectancy, and healthcare expenditure. The app utilizes a pre-trained machine learning model, PCA transformation, and data scaling to provide accurate predictions.

Features

User-friendly interface powered by Streamlit.

Predicts a country's development status as "Developed," "Developing," or "Under Developed."

Accepts inputs for:

Child mortality rate

Life expectancy

Total fertility rate

Percentage of GDP spent on health

Exports, imports, and other economic indicators

Utilizes pre-trained models and transformations stored in Pickle files.

Technologies Used

Python

Streamlit: For building the interactive web app.

Pandas: For data manipulation.

NumPy: For numerical computations.

Pickle: For loading the machine learning model and data transformers.

Files

app-2.py: The main script for running the Streamlit application.

model.pkl: Pre-trained machine learning model.

transformer.pkl: Data scaling transformer.

pca.pkl: PCA transformation for dimensionality reduction.

How to Run

Clone the repository:

git clone <repository_url>

Navigate to the project directory:

cd <repository_name>

Install the required Python libraries:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app-2.py

Open the application in your web browser at http://localhost:8501.

Inputs Required

The application requires the following inputs:

Child mortality rate

Life expectancy

Total fertility rate

Percentage of GDP spent on health

Economic indicators (e.g., exports, imports)

Outputs

The app provides a classification of a country's development status:

Developed

Developing

Under Developed

License

This project is licensed under the MIT License.
