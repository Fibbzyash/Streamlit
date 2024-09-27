# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# App title
st.title('House Price Prediction App')

# Input fields for dataset
st.subheader('Input Dataset')

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    st.write("Here's a preview of your dataset:")
    st.write(df.head())

    # Check if the required columns are available
    if {'area', 'bedrooms', 'bathrooms', 'price'}.issubset(df.columns):
        # User defines input features and target
        st.subheader('Training Features and Target')
        X = df[['area', 'bedrooms', 'bathrooms']]
        y = df['price']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Display training status
        st.success("Model trained successfully!")

        # Input fields for user to provide new house features for prediction
        st.subheader('Predict House Price')
        area = st.number_input('Area (in square feet)', min_value=500, max_value=5000, step=50)
        bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, step=1)
        bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=5, step=1)

        # Prediction button
        if st.button('Predict Price'):
            # Create an array for model input
            input_features = np.array([[area, bedrooms, bathrooms]])

            # Make prediction
            predicted_price = model.predict(input_features)

            # Display the result
            st.success(f'The predicted price for the house is ${predicted_price[0]:,.2f}')
    else:
        st.error("Dataset must contain 'area', 'bedrooms', 'bathrooms', and 'price' columns.")
else:
    st.info('Please upload a CSV file to train the model.')

