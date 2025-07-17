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

guideline_path = "data/cancer_guidelines.json"

# Load existing data
if os.path.exists(guideline_path):
    with open(guideline_path, "r") as f:
        try:
            cancer_guidelines = json.load(f)
        except json.JSONDecodeError:
            cancer_guidelines = []
else:
    cancer_guidelines = []

st.title("📘 Edit Cancer Guidelines")

# Get all existing cancer types + stages
entries = {(item["cancer_type"], item["stage"]): item for item in cancer_guidelines}

# --- Select or Add New Cancer Type/Stage ---
st.subheader("🔍 Select Cancer Type and Stage")
cancer_types = list(set([item["cancer_type"] for item in cancer_guidelines]))
selected_type = st.selectbox("Cancer Type", cancer_types + ["➕ Add new..."])

if selected_type == "➕ Add new...":
    selected_type = st.text_input("Enter new cancer type")

selected_stage = st.text_input("Enter Stage", value="II")

entry_key = (selected_type, selected_stage)

# Get or initialize regimens
entry = entries.get(entry_key, {"cancer_type": selected_type, "stage": selected_stage, "regimens": []})

st.markdown("---")
st.subheader(f"🧪 Regimens for {selected_type} (Stage {selected_stage})")

for i, regimen in enumerate(entry["regimens"]):
    with st.expander(f"Regimen {i+1}: {regimen['name']}"):
        regimen["name"] = st.text_input(f"Regimen Name {i+1}", regimen["name"], key=f"name_{i}")
        regimen["eligibility"] = st.text_area(f"Eligibility {i+1}", regimen.get("eligibility", ""), key=f"elig_{i}")
        regimen["efficacy"]["PFS"] = st.text_input(f"PFS {i+1}", regimen["efficacy"].get("PFS", ""), key=f"pfs_{i}")
        regimen["efficacy"]["OS"] = st.text_input(f"OS {i+1}", regimen["efficacy"].get("OS", ""), key=f"os_{i}")
        
        st.markdown("**Common Side Effects (%):**")
        for side_effect, value in regimen["side_effects"].items():
            new_value = st.text_input(f"{side_effect}", value, key=f"se_{i}_{side_effect}")
            regimen["side_effects"][side_effect] = new_value
        
        new_side = st.text_input(f"Add new side effect to Regimen {i+1}", key=f"addse_{i}")
        new_side_val = st.text_input(f"Percentage", key=f"addseval_{i}")
        if new_side and new_side_val:
            regimen["side_effects"][new_side] = new_side_val

        regimen["schedule"] = st.text_input(f"Schedule {i+1}", regimen.get("schedule", ""), key=f"sched_{i}")
        regimen["cost"] = st.number_input(f"Cost {i+1}", value=float(regimen.get("cost", 0)), key=f"cost_{i}")

# --- Add New Regimen ---
st.markdown("---")
st.subheader("➕ Add New Regimen")
if st.button("Add Empty Regimen"):
    entry["regimens"].append({
        "name": "New Regimen",
        "eligibility": "",
        "efficacy": {"PFS": "", "OS": ""},
        "side_effects": {},
        "schedule": "",
        "cost": 0
    })

# --- Save Changes ---
if st.button("💾 Save Guidelines"):
    # Update the original list
    updated = False
    for i, item in enumerate(cancer_guidelines):
        if item["cancer_type"] == selected_type and item["stage"] == selected_stage:
            cancer_guidelines[i] = entry
            updated = True
            break
    if not updated:
        cancer_guidelines.append(entry)

    with open(guideline_path, "w") as f:
        json.dump(cancer_guidelines, f, indent=2)
    st.success("✅ Guidelines updated and saved!")


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

# Drug Prices - editable table
st.subheader("💊 Edit Drug Prices")

price_path = os.path.join(DATA_DIR, "drug_prices.csv")
if os.path.exists(price_path):
    df_prices = pd.read_csv(price_path)
    edited_prices = st.data_editor(df_prices, num_rows="dynamic", use_container_width=True)
    if st.button("💾 Save Drug Prices"):
        edited_prices.to_csv(price_path, index=False)
        st.success("Drug prices saved!")


