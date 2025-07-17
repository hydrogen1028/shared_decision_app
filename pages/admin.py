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
