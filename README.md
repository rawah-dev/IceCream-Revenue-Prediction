 🍦 Ice Cream Revenue Predictor

An interactive Streamlit app that predicts daily ice cream revenue based on outside air temperature using a simple linear regression model.  
Proudly built by Rawah Al-Aqrabi 🇾🇪 to blend machine learning with real-time weather data.

 📊 Overview

This project uses **Simple Linear Regression** to model the relationship between temperature and ice cream sales.  
It allows users to:

- Upload custom datasets
- Visualize temperature vs. revenue
- Predict revenue based on input temperature
- Fetch live temperature using **OpenWeather API**

 🧠 Problem Statement

You own an ice cream business and want to forecast daily revenue in dollars based on the outside air temperature.  
A linear regression model is chosen to solve this problem.

- **Independent variable (X):** Outside Air Temperature  
- **Dependent variable (Y):** Daily revenue in dollars

To make predictions more dynamic, the app integrates **OpenWeather API** to fetch live temperature data based on city input.


🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/rawah-dev/IceCream-Revenue-Prediction.git
   cd IceCream-Revenue-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn scikit-learn requests python-dotenv
   ```

3. Create a `.env` file in the project root with your OpenWeather API key:
   ```
   OPENWEATHER_API_KEY=your_key_here
   ```
   Get a free key at [OpenWeatherMap](https://openweathermap.org/api).

4. Run the app:
   ```bash
   streamlit run ice_temp_model.py
   ```

---

Rawah Al-Aqrabi 🇾🇪 From Yemen | 💻 Passionate about AI, data-driven creativity, and technical identity 📬 GitHub: rawah-dev
