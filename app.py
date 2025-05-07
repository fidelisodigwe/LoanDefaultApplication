import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan.joblib")

# Create simple label encoders matching the model's training logic
education_map = {"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3, "Other": 4}
employment_map = {"Full-time": 0, "Part-time": 1, "Self-employed": 2, "Unemployed": 3}
marital_map = {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}
loan_purpose_map = {"Home": 0, "Car": 1, "Education": 2, "Business": 3, "Other": 4}

# Streamlit UI
st.title("Loan Default Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100)
income = st.number_input("Income", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)
months_employed = st.number_input("Months Employed", min_value=0)
num_credit_lines = st.number_input("Number of Credit Lines", min_value=0)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0)
loan_term = st.number_input("Loan Term (months)", min_value=1)
dti_ratio = st.number_input("DTI Ratio", min_value=0.0)

# Categorical inputs
education = st.selectbox("Education", list(education_map.keys()))
employment_type = st.selectbox("Employment Type", list(employment_map.keys()))
marital_status = st.selectbox("Marital Status", list(marital_map.keys()))
loan_purpose = st.selectbox("Loan Purpose", list(loan_purpose_map.keys()))
has_mortgage = st.selectbox("Has Mortgage", [0, 1])
has_dependents = st.selectbox("Has Dependents", [0, 1])
has_cosigner = st.selectbox("Has Co-Signer", [0, 1])

# Encode values
input_data = pd.DataFrame([{
    "Age": age,
    "Income": income,
    "LoanAmount": loan_amount,
    "CreditScore": credit_score,
    "MonthsEmployed": months_employed,
    "NumCreditLines": num_credit_lines,
    "InterestRate": interest_rate,
    "LoanTerm": loan_term,
    "DTIRatio": dti_ratio,
    "Education": education_map[education],
    "EmploymentType": employment_map[employment_type],
    "MaritalStatus": marital_map[marital_status],
    "HasMortgage": has_mortgage,
    "HasDependents": has_dependents,
    "LoanPurpose": loan_purpose_map[loan_purpose],
    "HasCoSigner": has_cosigner
}])

# Make prediction
if st.button("Predict Default"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Will Default (1)' if prediction[0] == 1 else 'Will Not Default (0)'}")
