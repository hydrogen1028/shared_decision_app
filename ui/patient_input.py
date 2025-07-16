import streamlit as st

def patient_input_form():
    with st.form("patient_form"):
        age = st.number_input("Age", min_value=18, max_value=100)
        sex = st.selectbox("Sex", ["Male", "Female"])
        weight = st.number_input("Weight (kg)")
        height = st.number_input("Height (cm)")
        ECOG = st.selectbox("ECOG Performance Status", [0, 1, 2, 3])
        cancer_type = st.selectbox("Cancer Type", ["lung cancer"])
        stage = st.selectbox("Stage", ["stage I", "stage II", "stage III", "stage IV"])
        concerns = st.text_area("Patient Concerns")
        comeds = st.text_input("Current Comedications (comma separated)")

        submitted = st.form_submit_button("Submit")
        if submitted:
            return {
                "age": age, "sex": sex, "weight": weight, "height": height,
                "ECOG": ECOG, "cancer_type": cancer_type, "stage": stage,
                "concerns": concerns, "comedications": comeds.split(",")
            }
