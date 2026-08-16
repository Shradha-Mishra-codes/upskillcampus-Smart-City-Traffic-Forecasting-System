# Smart City Traffic Pattern Forecasting System

AI-powered forecasting and analytics dashboard for smart-city traffic planning.

## Features (per docs)
- Upload CSV datasets
- Validate dataset schema (missing values, duplicates, columns)
- Automated EDA
- Data preprocessing + feature engineering
- Train and compare regression models
- Forecast future traffic
- Interactive analytics dashboard (Streamlit + Plotly)
- Download predictions and metrics

## Local Run

```bash
streamlit run app/app.py
```

## Project Structure
- `app/` Streamlit frontend (pages + components)
- `src/` backend modules (validation, preprocessing, training, forecasting, visualization)
- `config/` constants and configuration
- `models/` trained model artifacts
- `reports/` generated reports
- `data/` processed/uploads


