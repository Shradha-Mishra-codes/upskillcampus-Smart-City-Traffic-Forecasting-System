# coding_standards.md

# PURPOSE

This document defines coding standards that every file in this project must follow.

These rules are mandatory.

---

# PYTHON VERSION

Python 3.12

---

# STYLE GUIDE

Follow PEP8.

Maximum line length:

88 characters

Use Black formatting style.

Use Ruff compatible code.

---

# FILE NAMING

snake_case.py

Good

train_model.py

feature_engineering.py

dashboard.py

Bad

TrainModel.py

NEWFILE.py

abc.py

---

# CLASS NAMING

PascalCase

TrafficForecaster

DatasetValidator

ModelTrainer

---

# FUNCTION NAMING

snake_case

load_dataset()

train_model()

forecast_traffic()

calculate_metrics()

---

# VARIABLE NAMING

Use descriptive names.

Good

traffic_dataframe

forecast_result

trained_model

prediction_table

Bad

a

b

temp

new

test

---

# COMMENTS

Write comments only when necessary.

Avoid commenting obvious code.

Prefer self-documenting code.

---

# DOCSTRINGS

Every public function must include

Purpose

Parameters

Returns

Raises

Example

---

# IMPORTS

Standard Library

↓

Third-party Libraries

↓

Local Imports

Never use wildcard imports.

---

# LOGGING

Never use print() for debugging.

Always use logging.

Levels

INFO

WARNING

ERROR

CRITICAL

---

# CONFIGURATION

Never hardcode

paths

colors

magic numbers

Use config/constants.py.

---

# ERROR HANDLING

Always catch expected exceptions.

Display user-friendly errors.

Log technical details.

---

# REUSABILITY

Avoid duplicate code.

Create reusable helper functions.

Keep modules independent.

---

# PERFORMANCE

Vectorized Pandas.

Use caching.

Avoid nested loops.

Lazy loading where appropriate.

---

# SECURITY

Validate every uploaded CSV.

Sanitize filenames.

Never execute uploaded content.

---

# COMMIT FORMAT

feat:

fix:

docs:

style:

refactor:

test:

Example

feat: Added forecasting dashboard

fix: Corrected missing value handling

---

# FINAL GOAL

Maintain clean, maintainable, production-quality code.