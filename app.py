import streamlit as st
from ui.patient_input import patient_input_form
from logic.match_patient import get_matched_therapies
from ui.therapy_display import display_therapies
from logic.match_trials import match_trials  # <-- Add this line

st.title("🧬 Shared Decision-Making App for Anti-Cancer Therapy")

# 1. Input
patient_data = patient_input_form()

# 2. If data submitted, show therapy suggestions
if patient_data:
    suggestions = get_matched_therapies(patient_data)

    if suggestions:
        st.subheader("💊 Recommended Therapies")
        display_therapies(suggestions)
    else:
        st.warning("⚠️ No standard therapies matched for this patient.")

    # 3. Show matched clinical trials
    trial_matches = match_trials(patient_data)
    if not trial_matches.empty:
        st.subheader("🧪 Eligible Clinical Trials")
        for _, trial in trial_matches.iterrows():
            st.markdown(f"**{trial['trial_name']}** — {trial['custom_note']}")
    else:
        st.info("No matched clinical trials for this profile.")

import streamlit as st

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


