# 🎓 Student Placement Prediction System

A machine learning web application that predicts whether a student is likely to be placed based on key academic and skill-based inputs. Built using **Streamlit** and a **Decision Tree model**, this project provides an interactive interface for real-time predictions.

---

## 🚀 Features

* 📊 Interactive UI using Streamlit
* 🤖 Machine Learning model (Decision Tree)
* 🎯 Real-time placement prediction
* 📈 Displays prediction confidence (if available)
* 🧾 User-friendly input system (sliders, dropdowns)
* 🔄 Reset functionality
* 📂 Dataset preview inside app

---

## 🧠 Input Parameters

The prediction is based on the following inputs:

* IQ Score
* Academic Performance
* Internship Experience
* CGPA Level (Low / Medium / High)
* Communication Skills (Low / Medium / High)
* Number of Projects (Low / Medium / High)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib

---

## 📁 Project Structure

```
├── app.py                  # Main Streamlit app
├── tree.joblib            # Trained Decision Tree model
├── columns.joblib         # Training columns for alignment
├── data.joblib            # Dataset used in app preview
├── dataset.csv            # Raw dataset (optional)
├── notebooks/             # Jupyter notebooks (EDA & model)
└── README.md              # Project documentation
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the project folder:

```
cd your-repo-name
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the Streamlit app:

```
streamlit run app.py
```

---

## 📌 How It Works

* User inputs are collected via the Streamlit UI
* Inputs are converted into a DataFrame
* One-hot encoding is applied
* Data is aligned with training columns
* The trained model predicts placement outcome

---

## 📊 Model Details

* Algorithm: Decision Tree Classifier
* Handles categorical + numerical features
* Outputs binary prediction:

  * 🎉 Placed
  * ⚠️ Not Placed

---

## 📷 App Preview

> Add screenshots here for better presentation

---

## 💡 Future Improvements

* Add more ML models (Random Forest, XGBoost)
* Improve UI/UX design
* Add login system
* Deploy on cloud (Streamlit Cloud / AWS / Render)
* Add analytics dashboard

---

## 👨‍💻 Author

**Varun Sharma**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
