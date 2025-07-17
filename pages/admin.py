import streamlit as st
import pandas as pd
import json
import os

st.title("🛠 Admin Panel: Update Data Files")

DATA_DIR = "data"

# Upload recommended therapies
st.subheader("📘 Upload Cancer Guidelines (JSON)")
guidelines_file = st.file_uploader("Upload new cancer_guidelines.json", type=["json"])
if guidelines_file is not None:
    guidelines_path = os.path.join(DATA_DIR, "cancer_guidelines.json")
    with open(guidelines_path, "wb") as f:
        f.write(guidelines_file.read())
    st.success("✅ Cancer guidelines updated!")


GUIDELINE_PATH = "data/cancer_guidelines.json"

# Load guidelines
def load_guidelines():
    try:
        with open(GUIDELINE_PATH, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception as e:
        st.warning(f"Could not load guidelines: {e}")
    return []

# Save guidelines
def save_guidelines(data):
    try:
        with open(GUIDELINE_PATH, "w") as f:
            json.dump(data, f, indent=2)
        st.success("✅ Saved successfully!")
    except Exception as e:
        st.error(f"❌ Failed to save: {e}")

# Load current
guidelines = load_guidelines()

st.title("📋 Edit Recommended Anti-Cancer Regimens")

# Form to add new entry
from utils.side_effects import load_common_side_effects, save_common_side_effect

# Load the common side effects
common_side_effects = load_common_side_effects()

# Inside your main regimen form
with st.form("add_regimen_form"):
    st.subheader("🧪 Add New Regimen")

    # Basic regimen fields
    cancer_type = st.text_input("Cancer Type")
    stage = st.text_input("Stage")
    regimen_name = st.text_input("Regimen Name")
    efficacy_os = st.text_input("Overall Survival (OS)")
    efficacy_pfs = st.text_input("Progression-Free Survival (PFS)")
    schedule = st.text_area("Schedule and Dose")
    price = st.number_input("Estimated Price", min_value=0.0)

    # 🔽 Side Effect Section
    st.markdown("### 📉 Common Side Effects")
    side_effects_dict = {}
    num_effects = st.number_input("Number of Side Effects", min_value=0, max_value=10, step=1, key="n_effects")

    for i in range(num_effects):
        cols = st.columns([2, 1, 1])
        with cols[0]:
            effect = st.selectbox(
                f"Side Effect #{i+1}",
                options=[""] + common_side_effects,
                key=f"effect_{i}",
            )
            custom_effect = st.text_input("Or type a new side effect", key=f"custom_effect_{i}")
            if custom_effect:
                effect = custom_effect.strip()
        with cols[1]:
            severity = st.selectbox("Grade", options=["1", "2", "3", "4", "5"], key=f"grade_{i}")
        with cols[2]:
            percent = st.text_input("Percent (%)", key=f"percent_{i}")

        if effect:
            side_effects_dict[effect] = {
                "grade": severity,
                "percent": percent
            }

    # Form submission
    submitted = st.form_submit_button("✅ Add Regimen")

    if submitted:
        if cancer_type and stage and regimen_name:
            # Add side effect to persistent list
            for effect in side_effects_dict:
                save_common_side_effect(effect)

            new_entry = {
                "cancer_type": cancer_type,
                "stage": stage,
                "regimen": regimen_name,
                "efficacy": {
                    "OS": efficacy_os,
                    "PFS": efficacy_pfs,
                },
                "schedule": schedule,
                "price": price,
                "side_effects": side_effects_dict,
            }

            # Append new_entry to JSON file
            with open("data/cancer_guidelines.json", "r") as f:
                data = json.load(f)
            data.append(new_entry)
            with open("data/cancer_guidelines.json", "w") as f:
                json.dump(data, f, indent=2)

            st.success("✅ Regimen added successfully!")
        else:
            st.error("Please fill in all required fields.")

   

# Show current data
st.subheader("📖 Current Regimens")
for entry in guidelines:
    with st.expander(f"{entry['cancer_type']} – Stage {entry['stage']}"):
        for regimen in entry["regimens"]:
            st.markdown(f"- **{regimen['name']}**")
            st.markdown(f"  - Eligibility: {regimen['eligibility']}")
            st.markdown(f"  - Efficacy: PFS={regimen['efficacy'].get('PFS')}, OS={regimen['efficacy'].get('OS')}")
            st.markdown(f"  - Schedule: {regimen['schedule']}")
            st.markdown(f"  - Cost: {regimen['cost']}")
            st.markdown("  - Side Effects:")
            for k, v in regimen["side_effects"].items():
                st.markdown(f"    - {k}: {v}")

# Upload clinical trials
st.subheader("🧪 Upload Clinical Trials (CSV)")
trials_file = st.file_uploader("Upload new clinical_trials.csv", type=["csv"])
if trials_file is not None:
    trials_path = os.path.join(DATA_DIR, "clinical_trials.csv")
    with open(trials_path, "wb") as f:
        f.write(trials_file.read())
    st.success("✅ Clinical trials updated!")

# Upload drug prices
st.subheader("💰 Upload Drug Prices (CSV)")
prices_file = st.file_uploader("Upload new drug_prices.csv", type=["csv"])
if prices_file is not None:
    prices_path = os.path.join(DATA_DIR, "drug_prices.csv")
    with open(prices_path, "wb") as f:
        f.write(prices_file.read())
    st.success("✅ Drug prices updated!")


