# 📊 Student Performance Analysis & Final Score Prediction

This project is built using **Python, Data Science, and Machine Learning techniques** to analyze student performance and predict their final scores based on features such as study hours, attendance, previous scores, and participation.

---

## 🧠 Objective

To understand the key factors affecting student academic performance and build a **predictive model** to estimate the final score using regression techniques.

---

## 📁 Dataset

We used a **custom dataset** with the following features:

| Feature       | Description                        |
| ------------- | ---------------------------------- |
| Name          | Student's name                     |
| StudyHours    | Daily study hours                  |
| Attendance    | Percentage of attendance           |
| PreviousScore | Score in the previous exam (%)     |
| Participation | Co-curricular participation score  |
| FinalScore    | Final exam score (target variable) |

> 📌 No missing values were present in the dataset. If future updates introduce nulls, appropriate imputation strategies will be used (mean/median/forward-fill based on feature type).

---

## 🧪 Exploratory Data Analysis (EDA)

- Distribution of all numeric variables
- Summary statistics: mean, median, std, quartiles
- **Correlation heatmap** showed:
  - Positive correlation between study hours, attendance, previous scores, participation, and final score.
  - Attendance had the strongest correlation with final score.

---

## 🤖 Machine Learning Model

We used **Linear Regression** to build a predictive model.

### 🔧 Model Inputs

- `StudyHours`
- `Attendance`
- `PreviousScore`
- `Participation`

### 🎯 Model Output

- `Predicted Final Score`

### 🧪 Evaluation Metrics

- Mean Squared Error (MSE)
- R-squared Score (R2)

> 🎓 At default (0s for all inputs), the model predicted around **16.5**, showing the intercept influence.

---

## 🌐 Web App with Streamlit

A simple **Streamlit web interface** was built to:

- Input values for a new student
- Predict the final score in real-time

To run the app:

```bash
streamlit run app.py
```

---

## ✅ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
student-performance-ml/
├── app.py
├── student_data.csv
├── model.pkl
├── Student_Performance_Analysis.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧑 Author

Neeraj Singh

---

Feel free to fork, use, or improve this project. ⭐ it if you like it!