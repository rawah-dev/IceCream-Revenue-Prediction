import os

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
import streamlit as st
from dotenv import load_dotenv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

load_dotenv()

st.title("📊 Ice Cream Revenue Predictor by Rawah")

api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    st.warning(
        "OpenWeather API key not found. Copy `.env.example` to `.env` "
        "and add your key to enable live weather predictions."
    )

# 📥 Upload CSV
uploaded_file = st.file_uploader("Upload IceCreamData.csv", type="csv")
if uploaded_file:
    Icecream = pd.read_csv(uploaded_file)
    st.write("📄 Original Data:", Icecream)

    st.subheader("📈 Data Analysis")
    st.write(Icecream.describe())

    st.subheader("📊 Visualizations")
    fig1 = sns.jointplot(x='Revenue', y='Temperature', data=Icecream, color='purple')
    st.pyplot(fig1.figure)

    fig2 = sns.pairplot(Icecream)
    st.pyplot(fig2)

    fig3 = sns.lmplot(x='Temperature', y='Revenue', data=Icecream)
    st.pyplot(fig3.figure)

    # 📊 Model Training
    X = Icecream[['Temperature']]
    y = Icecream[['Revenue']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
    regressor = LinearRegression(fit_intercept=True)
    regressor.fit(X_train, y_train)

    st.subheader("📐 Model Results")
    st.write("Coefficient (m):", regressor.coef_)
    st.write("Intercept (b):", regressor.intercept_)

    st.subheader("📉 Training Plot")
    fig4, ax = plt.subplots()
    ax.scatter(X_train, y_train, color='green')
    ax.plot(X_train, regressor.predict(X_train), color='red')
    ax.set_xlabel('Temperature [°C]')
    ax.set_ylabel('Revenue [$]')
    ax.set_title('Revenue vs Temperature (Training)')
    st.pyplot(fig4)

    # 🌍 Get Temperature from City
    st.subheader("🌍 Get Temperature from City Name")
    city = st.text_input("Enter city name:", "")
    if city.strip():
        if not api_key:
            st.error("Cannot fetch weather: OPENWEATHER_API_KEY is missing from `.env`.")
        else:
            query_city = "Ta'izz" if city.strip().lower() == "taiz" else city.strip()
            url = (
                "http://api.openweathermap.org/data/2.5/weather"
                f"?q={query_city}&appid={api_key}&units=metric"
            )
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                st.success(f"Current temperature in {city} is {temp}°C")

                Temp = pd.DataFrame([[temp]], columns=["Temperature"])
                Revenue = regressor.predict(Temp)
                st.write(f"Expected revenue at {temp}°C is: ${Revenue[0][0]:.2f}")
            else:
                st.error("City not found or API error.")
