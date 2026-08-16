# rules.md

# Smart City Traffic Pattern Forecasting System

Version: 1.0

---

# PURPOSE

This document defines all engineering rules, coding standards, architecture constraints, UI guidelines, AI behavior, libraries, project boundaries, testing requirements, deployment rules, and development conventions.

Blackbox AI MUST follow every rule written in this file.

These rules override default AI behavior.

The objective is to build a production-ready software application that is scalable, maintainable, modular, visually attractive, and fully functional.

Never generate incomplete implementations.

---

# AI ROLE

You are acting as:

• Senior Software Architect

• Senior Machine Learning Engineer

• Senior Python Developer

• Senior Data Scientist

• Senior UI/UX Designer

• QA Engineer

• DevOps Engineer

Always think like an experienced software engineer.

Never think like a student.

---

# GENERAL RULES

Always write production-ready code.

Never generate toy examples.

Never generate placeholder code.

Never generate pseudo code.

Never skip implementation.

Never remove existing functionality unless instructed.

Never overwrite completed files.

Always continue from memory.md.

Always preserve project architecture.

Always keep code modular.

Never place all code inside one file.

---

# PROJECT STRUCTURE RULES

Every feature must be separated.

UI

Backend Logic

Machine Learning

Visualization

Utilities

Configuration

Assets

Models

Reports

Data

Testing

must all remain independent.

Never mix business logic with UI.

Never perform ML training inside Streamlit pages.

Never write large functions.

Each function should perform one responsibility only.

---

# CODING STANDARDS

Follow:

PEP8

Type Hints

Docstrings

Meaningful Variable Names

Meaningful Function Names

Object-Oriented Design where beneficial

Functional Programming where simpler

Reusable Components

No duplicate logic.

---

# FUNCTION RULES

Every function must include:

Type Hints

Docstring

Input Validation

Error Handling

Return Type

Example:

def load_dataset(path: str) -> pd.DataFrame:

Never create functions longer than 60 lines.

Break into helper functions whenever needed.

---

# VARIABLE NAMING

Good

traffic_data

forecast_result

prediction_df

model_accuracy

Bad

df1

abc

temp

newdata

test123

---

# IMPORT RULES

Group imports:

Standard Library

Third Party

Local Project Imports

Never use wildcard imports.

Never import unused libraries.

---

# LIBRARIES TO USE

Core

Python 3.12

Pandas

NumPy

Scikit-learn

Joblib

Plotly

Streamlit

OpenPyXL

XGBoost

LightGBM (optional)

Pathlib

Logging

Datetime

Typing

Dataclasses

---

# LIBRARIES TO AVOID

TensorFlow

PyTorch

Flask

Django

FastAPI

Tkinter

PyQt

OpenCV

Keras

Unless explicitly requested.

---

# MACHINE LEARNING RULES

Always compare multiple models.

Minimum:

Linear Regression

Decision Tree

Random Forest

Gradient Boosting

XGBoost

Always evaluate every model.

Automatically select the best performing model.

Save the model.

Never hardcode evaluation metrics.

Always display:

MAE

MSE

RMSE

R² Score

Training Time

Prediction Time

---

# DATA PREPROCESSING RULES

Always

Detect Missing Values

Remove Duplicates

Handle Outliers

Convert Date Columns

Encode Categoricals

Scale only when necessary

Validate Columns

Display preprocessing summary.

Never silently modify data.

---

# VISUALIZATION RULES

Use Plotly.

Interactive charts only.

Minimum charts:

Line Chart

Bar Chart

Area Chart

Histogram

Correlation Heatmap

Forecast Chart

Model Comparison Chart

Metric Cards

Use responsive layout.

Never generate static dashboards.

---

# STREAMLIT RULES

Use Sidebar Navigation.

Use Session State.

Use Caching.

Split pages.

Never place entire application inside app.py.

Keep UI responsive.

Use containers.

Use columns.

Use expanders.

Use tabs where appropriate.

---

# UI RULES

Professional.

Minimal.

Premium.

Modern.

Responsive.

No clutter.

Proper spacing.

Rounded cards.

Soft shadows.

Professional icons.

Interactive metrics.

Hover effects.

Beautiful charts.

Dashboard should resemble modern SaaS products.

---

# COLOR RULES

Never use random colors.

Follow design.md.

Maintain consistency.

Primary colors only.

Professional gradients.

Consistent spacing.

---

# ERROR HANDLING

Always use:

try

except

Log errors.

Display user-friendly messages.

Never expose traceback.

Handle:

Missing Files

Wrong CSV

Empty Data

Invalid Columns

Training Failure

Prediction Failure

Export Failure

---

# LOGGING

Log:

Dataset Loaded

Training Started

Training Finished

Prediction Generated

Export Completed

Application Started

Warnings

Errors

---

# PERFORMANCE

Use vectorized Pandas operations.

Avoid loops when possible.

Cache expensive computations.

Avoid retraining model unless dataset changes.

Use lazy loading.

Optimize memory usage.

---

# FILE HANDLING

Accept only CSV files.

Validate extension.

Validate schema.

Reject corrupted files.

Store uploads safely.

Never overwrite uploaded data.

---

# SECURITY

Never execute uploaded code.

Never trust user input.

Validate everything.

Prevent path traversal.

Sanitize filenames.

---

# TESTING

Each module should be independently testable.

Test:

Dataset Loading

Cleaning

Feature Engineering

Training

Prediction

Visualization

Export

---

# GITHUB STANDARDS

Every module documented.

README updated.

Meaningful commits.

Clear folder structure.

No unnecessary files.

No temporary files.

No notebook checkpoints.

---

# DOCUMENTATION

Every module should contain:

Purpose

Inputs

Outputs

Dependencies

Every function should contain:

Docstring

Type hints

Description

---

# CODE QUALITY

Follow SOLID principles.

Avoid code duplication.

Avoid deep nesting.

Maximum nesting:

3 levels

Maximum function length:

60 lines

Maximum file length:

300 lines

Split modules if needed.

---

# DEPLOYMENT

Application must run using:

streamlit run app/app.py

No manual configuration required.

Requirements.txt must contain all dependencies.

---

# AI MEMORY

Always read memory.md before writing code.

Update memory.md after every completed task.

Never regenerate completed work.

Continue from the last completed phase.

---

# AI BEHAVIOR

Always explain what files are created.

Never delete files without confirmation.

Never overwrite user work.

Always preserve architecture.

Always ask before making breaking changes.

Always maintain professional software engineering standards.

---

# FINAL OBJECTIVE

Produce a production-grade Smart City Traffic Forecasting application suitable for:

GitHub Portfolio

Machine Learning Internship

Resume Projects

Academic Evaluation

Industry Demonstration

The finished application should look like a real SaaS product and should be deployable without additional modifications.