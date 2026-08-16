# testing.md

# TESTING STRATEGY

Testing is required after every completed phase.

---

# UNIT TESTS

Dataset Loading

CSV Validation

Missing Value Detection

Duplicate Removal

Feature Engineering

Model Training

Prediction

Model Saving

Visualization

Download CSV

---

# INTEGRATION TESTS

Upload Dataset

↓

EDA

↓

Preprocessing

↓

Training

↓

Forecast

↓

Dashboard

Everything should work without failure.

---

# UI TESTS

Sidebar Navigation

Buttons

Charts

Filters

Dropdowns

Date Pickers

Downloads

Responsive Layout

---

# ERROR TESTS

Wrong CSV

Missing Columns

Corrupted File

Empty Dataset

Model Failure

Prediction Failure

---

# PERFORMANCE TESTS

Dataset Load < 3 sec

Prediction < 2 sec

Dashboard Render < 2 sec

---

# ACCEPTANCE TEST

Application should run with

streamlit run app/app.py

without errors.

No warnings.

No crashes.