# 🎓 Student Placement Prediction System (ML + Streamlit Dashboard)

## 📄 Description

A machine learning-powered web application that predicts whether a student is likely to be placed based on academic and skill-based inputs.

This project uses a Decision Tree model trained on student placement data and provides an interactive Streamlit dashboard for real-time predictions. It also includes complete data analysis, database integration, and visualization workflows.

The system allows users to input parameters like IQ, academic performance, internships, communication skills, CGPA, and projects to generate placement predictions along with confidence scores.

---

## 🚀 Features

* 🔮 Real-time placement prediction using ML model
* 📊 Interactive Streamlit dashboard
* 📁 Data preprocessing & EDA (Jupyter Notebooks)
* 🗄️ MySQL database integration
* 📈 Power BI dashboard for visualization
* ⚡ Fast and user-friendly UI

---

## 🧠 Machine Learning Model

* Model Used: Decision Tree Classifier

### Input Features:

* IQ Score
* Academic Performance
* Internship Experience
* CGPA (Categorized)
* Communication Skills
* Projects

### Output:

* Likely to be Placed
* Not Likely to be Placed

Model also provides prediction confidence.

---

## 🖥️ Streamlit App

Main application file:
app.py 

### Features:

* Sidebar input controls
* Real-time prediction
* Probability display
* Reset functionality
* Dataset preview

---

## 📂 Project Structure

```
├── app.py                    # Streamlit application
├── data.joblib              # Processed dataset
├── tree.joblib              # Trained ML model
├── columns.joblib           # Training column structure
├── cspd_cleaned.csv         # Clean dataset
├── college_student_placement_dataset.csv
├── cspd_eda.ipynb           # Data analysis
├── cspd_mysql_db.ipynb      # Database integration
├── cspd.sql                 # SQL schema
├── cspd_PBI.pbix            # Power BI dashboard
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/placement-predictor.git
cd placement-predictor
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
streamlit run app.py
```

---

## 🧪 How It Works

1. User inputs student details
2. Data is converted using one-hot encoding
3. Input is aligned with training columns
4. Model predicts placement outcome
5. Results + confidence displayed

---

## 📊 Dataset

The dataset contains student academic and skill attributes used to predict placement outcomes.

---

## 📈 Visualization

* Power BI dashboard included
* Shows trends, insights, and feature importance

---

## 🗄️ Database

* MySQL integration using SQL scripts
* Stores and manages structured data

---

## 💡 Future Improvements

* Add more ML models (Random Forest, XGBoost)
* Improve UI/UX design
* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Add authentication system
* Real-time data integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Developed by **Varun Sharma**
