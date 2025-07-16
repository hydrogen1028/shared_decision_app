import streamlit as st
from ui.patient_input import patient_input_form
from logic.match_patient import get_matched_therapies
from ui.therapy_display import display_therapies

st.title("🧬 Shared Decision Support for Anti-Cancer Therapy")

# 1. Input
patient_data = patient_input_form()

# 2. Therapy suggestions
if patient_data:
    suggestions = get_matched_therapies(patient_data)
    if suggestions:
        display_therapies(suggestions)
    else:
        st.warning("No therapies matched for this input. Please review criteria.")
