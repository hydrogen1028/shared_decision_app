import streamlit as st
import pandas as pd

def admin_tools():
    st.header("⚙️ Admin Panel")

    st.subheader("🧪 Clinical Trials Editor")
    trials = pd.read_csv("data/clinical_trials.csv")
    edited_trials = st.experimental_data_editor(trials, num_rows="dynamic")
    if st.button("💾 Save Clinical Trials"):
        edited_trials.to_csv("data/clinical_trials.csv", index=False)
        st.success("Clinical trials updated.")

    st.subheader("💰 Drug Price Editor")
    prices = pd.read_csv("data/drug_prices.csv")
    edited_prices = st.experimental_data_editor(prices, num_rows="dynamic")
    if st.button("💾 Save Prices"):
        edited_prices.to_csv("data/drug_prices.csv", index=False)
        st.success("Drug prices updated.")
