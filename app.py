import streamlit as st
import pandas as pd
from joblib import load
import os

# ---------------- SAFE LOAD ----------------
def safe_load(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, filename)

    if not os.path.exists(full_path):
        st.error(f"❌ Missing file: {filename}")
        st.write("📁 Files:", os.listdir(base_path))
        st.stop()

    return load(full_path)

# ---------------- LOAD FILES ----------------
model = safe_load('tree.joblib')
train_cols = safe_load('columns.joblib')
data = safe_load('data.joblib')

# fix column type
if not isinstance(train_cols, list):
    train_cols = list(train_cols)

# ---------------- PAGE ----------------
st.set_page_config(page_title="Placement Predictor", layout="wide")

st.title("🎓 Student Placement Prediction System")
st.markdown("### Decision Tree Model")
st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.header("📊 Student Inputs")

IQ = st.sidebar.slider("IQ Score", 80, 150, 100)
Academic_Performance = st.sidebar.slider("Academic Performance", 0, 10, 7)
Internship = st.sidebar.radio("Internship Experience", ["No", "Yes"])

# ---------------- INPUT ----------------
# ---------------- INPUT ----------------
st.subheader("🧾 Student Profile")

col1, col2, col3 = st.columns(3)

with col1:
    CGPA_bin = st.selectbox(
        "CGPA (0–6 Low | 6–7.5 Medium | 7.5–10 High)",
        ["Low", "Medium", "High"],
        key="cgpa"
    )

with col2:
    Comm_bin = st.selectbox(
        "Communication (0–4 Low | 4–7 Medium | 7–10 High)",
        ["Low", "Medium", "High"],
        key="comm"
    )

with col3:
    Projects_bin = st.selectbox(
        "Projects (0–1 Low | 2–3 Medium | 4+ High)",
        ["Low", "Medium", "High"],
        key="proj"
    )

# ---------------- CREATE INPUT ----------------
input_df = pd.DataFrame({
    'IQ': [IQ],
    'Academic_Performance': [Academic_Performance],
    'Internship_Experience': [Internship],
    'CGPA_bin': [CGPA_bin],
    'Comm_bin': [Comm_bin],
    'Projects_bin': [Projects_bin]
})

# ---------------- IMPORTANT FIX ----------------
# NO drop_first here
input_df = pd.get_dummies(input_df)

# ---------------- ALIGN ----------------
input_df = input_df.reindex(columns=train_cols, fill_value=0)

# ---------------- PREDICTION ----------------
st.subheader("🔮 Prediction")

if st.button("Predict"):
    try:
        pred = model.predict(input_df)[0]

        # show probability (debug)
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_df)[0]
            st.write("Confidence:", prob)

        if pred == 1:
            st.success("🎉 Likely to be Placed")
        else:
            st.error("⚠️ Not Likely to be Placed")

    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- RESET ----------------
if st.button("Reset"):
    st.session_state.clear()
    st.rerun()

# ---------------- OUTPUT ----------------
st.divider()
st.subheader("📋 Input Data")
st.dataframe(input_df)

with st.expander("📊 Dataset Preview"):
    st.dataframe(data.head())