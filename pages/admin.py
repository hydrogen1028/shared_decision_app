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

import streamlit as st
import json
import os

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
st.subheader("➕ Add New Cancer Regimen")
with st.form("add_regimen_form"):
    cancer_type = st.text_input("Cancer Type")
    stage = st.text_input("Stage")
    name = st.text_input("Regimen Name")
    eligibility = st.text_input("Eligibility Criteria")
    pfs = st.text_input("PFS")
    os_val = st.text_input("OS")
    schedule = st.text_input("Schedule")
    cost = st.number_input("Estimated Cost", min_value=0)

    st.markdown("### Side Effects Input")
    side_effects_dict = {}
    num_effects = st.number_input("Number of Common Side Effects", min_value=0, max_value=10, step=1)

    for i in range(num_effects):
        cols = st.columns([2, 1])
        with cols[0]:
            effect = st.text_input(f"Side Effect #{i+1}", key=f"effect_{i}")
        with cols[1]:
            percent = st.text_input(f"%", key=f"percent_{i}")
        if effect:
            side_effects_dict[effect] = percent

    submitted = st.form_submit_button("Add Regimen")

    if submitted:
        # Check if entry exists
        found = False
        for entry in guidelines:
            if entry["cancer_type"] == cancer_type and entry["stage"] == stage:
                entry["regimens"].append({
                    "name": name,
                    "eligibility": eligibility,
                    "efficacy": {"PFS": pfs, "OS": os_val},
                    "side_effects": side_effects_dict,
                    "schedule": schedule,
                    "cost": cost
                })
                found = True
                break

        if not found:
            guidelines.append({
                "cancer_type": cancer_type,
                "stage": stage,
                "regimens": [{
                    "name": name,
                    "eligibility": eligibility,
                    "efficacy": {"PFS": pfs, "OS": os_val},
                    "side_effects": side_effects_dict,
                    "schedule": schedule,
                    "cost": cost
                }]
            })

        save_guidelines(guidelines)

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


