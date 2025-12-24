# 🎯 Productivity Prediction Engine

An end-to-end machine learning project that predicts **session-level productivity**
based on mood, sleep, focus level, task type, and music choice.

This project demonstrates the complete ML workflow — from data generation and
exploratory analysis to model training, evaluation, and deployment using Streamlit.

---

## 🚀 Project Overview

Productivity is influenced by both **psychological** and **contextual** factors.
This project models those relationships to answer:

> *How productive is a person likely to be in a given work session?*

Each data point represents **one focused work session**.

---

## 📊 Dataset

The dataset is **synthetically generated** using rule-based logic to simulate
realistic productivity behavior.

### Features:
- `mood` — emotional state (happy, calm, stressed, anxious, sad)
- `sleep_hours` — hours of sleep before the session
- `focus_level` — self-reported focus (1–10)
- `task_type` — type of work (coding, study, routine, creative)
- `music_type` — background audio (lofi, instrumental, lyrical, silence)

### Target:
- `productivity_score` — productivity score (0–100)

The data generation logic embeds realistic assumptions such as:
- Focus being the primary driver of productivity
- Sleep affecting performance non-linearly
- Music type interacting with task type (e.g., lyrical music during coding)

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was used to:
- Validate data generation assumptions
- Understand feature distributions
- Analyze interactions (e.g., task type vs music type)

Key insights from EDA directly informed model expectations.

---

## 🤖 Models Used

### 1. Linear Regression (Baseline)
- Provides interpretability and a strong baseline
- Assumes linear relationships between features and productivity

### 2. Random Forest Regressor (Advanced Model)
- Captures non-linear relationships and feature interactions
- Significantly improves predictive performance

---

## 📈 Model Evaluation

Evaluation metrics:
- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**

| Model              | MAE ↓ | RMSE ↓ |
|--------------------|------|--------|
| Linear Regression  | ~5.7 | ~7.6   |
| Random Forest      | ~2.3 | ~3.7   |

The improvement confirms the presence of non-linear interactions in the data.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn (EDA)

---

## 🌐 Streamlit Application

An interactive Streamlit app allows users to:
- Select mood, task type, and music
- Adjust sleep hours and focus level
- Instantly receive a predicted productivity score

The app uses the **Random Forest model** for inference.

---

## ▶️ How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
