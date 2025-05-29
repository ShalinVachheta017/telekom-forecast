

# 📊 Telecom Finance Forecasting (In Progress)

This project aims to forecast and analyze key financial KPIs in the telecom industry using advanced data science methodologies. Built using real-world data from the Kaggle Telecom Revenue Assurance Dataset, this work aligns with the Deutsche Telekom “Start up!” trainee program, emphasizing finance, analytics, and actionable business outcomes.

---

## 🎯 Objectives

- Forecast telecom revenue trends using time-series models (Prophet, ARIMA)
- Engineer meaningful KPIs: ARPU, ROI, Plan Mix, Revenue per Usage Unit
- Train ML models (Random Forest, XGBoost) for revenue prediction
- Visualize results in an interactive Streamlit dashboard
- Deploy the pipeline using Docker for portability and reproducibility

---

## 🗃️ Dataset

**Source**: [Kaggle - Telecom Revenue Assurance Dataset](https://www.kaggle.com/datasets/manasatoorpu/telecom-revenue)  
**Contains**: Call duration, data usage, subscription plan, billing anomaly

---

## 🧱 Project Structure

```

telekom\_forecast\_project/
├── data/                  # Raw and processed data files
├── src/telekom\_forecast/  # Core processing and models
│   ├── assign\_revenue.py
│   ├── generate\_monthly\_data.py
│   ├── forecast\_revenue.py
│   ├── ml\_model\_training.py
│   └── logging/logger.py
├── notebooks/             # EDA and KPI analysis
│   └── EDA\_Financial\_KPIs.ipynb
├── streamlit\_app/         # Dashboard
│   └── app.py
├── models/                # Saved model artifacts
├── logs/                  # Run logs and error traces
├── requirements.txt       # Python dependencies
├── Dockerfile             # Deployment container
└── README.md              # This file

````

---

## 🚀 Running the Project

### 1. Clone and install dependencies:
```bash
git clone https://github.com/<your-username>/telekom-forecast-project.git
cd telekom-forecast-project
pip install -r requirements.txt
````

### 2. Run the pipeline

```bash
python src/telekom_forecast/assign_revenue.py
python src/telekom_forecast/generate_monthly_data.py
python src/telekom_forecast/forecast_revenue.py
python src/telekom_forecast/ml_model_training.py
```

### 3. Launch Streamlit dashboard

```bash
streamlit run streamlit_app/app.py
```

---

## 🐳 Docker (Optional)

```bash
docker build -t telecom_forecast .
docker run -p 8501:8501 telecom_forecast
```

---

## 📈 Technologies Used

* **Python**, **Pandas**, **NumPy**
* **Prophet**, **ARIMA**, **XGBoost**, **scikit-learn**
* **Plotly**, **Streamlit**, **SHAP**
* **Docker**, **VS Code**, **Git**

---

## 👨‍💼 Author

**Shalin Vachheta**
M.Sc. Mechatronics, University of Siegen
Passionate about AI for Finance, Explainable ML, and Generative Intelligence
📫 [LinkedIn](https://www.linkedin.com/in/shalinvachheta017)

````
