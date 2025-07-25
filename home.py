import streamlit as st
from ui.patient_input import patient_input_form
from logic.match_patient import get_matched_therapies
from logic.match_trials import match_trials
from ui.therapy_display import display_therapies

st.title("🧬 Shared Decision Support for Anti-Cancer Therapy")

# 1. Input
patient_data = patient_input_form()
trial_matches = match_trials(patient_data)

# 2. Therapy suggestions
if patient_data:
    suggestions = get_matched_therapies(patient_data)
    if suggestions:
        display_therapies(suggestions)
    else:
        st.warning("No therapies matched for this input. Please review criteria.")

if not trial_matches.empty:
    st.subheader("🧪 Eligible Clinical Trials")
    for _, trial in trial_matches.iterrows():
        st.markdown(f"**{trial['trial_name']}** — {trial['custom_note']}")

# Fake login
st.sidebar.title("🔐 Admin Access")
admin_mode = st.sidebar.checkbox("Admin Mode")
if admin_mode:
    password = st.sidebar.text_input("Enter Admin Password", type="password")
    if password == "mysecret123":
        from ui.admin_panel import admin_tools
        admin_tools()
    else:
        st.sidebar.warning("Incorrect password.")


