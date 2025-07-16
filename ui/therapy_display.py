import streamlit as st
import plotly.graph_objects as go

def display_therapies(therapies):
    for t in therapies:
        st.subheader(t["name"])
        st.markdown(f"**Eligibility**: Age {t['eligibility']['age'][0]}–{t['eligibility']['age'][1]}, ECOG {t['eligibility']['ECOG']}")
        st.markdown(f"**Efficacy**: PFS = {t['efficacy']['PFS']}, OS = {t['efficacy']['OS']}")
        
        st.markdown("**Side Effects:**")
        fig = go.Figure(go.Bar(
            x=list(t['side_effects'].values()),
            y=list(t['side_effects'].keys()),
            orientation='h'
        ))
        st.plotly_chart(fig)

        st.markdown(f"**Schedule**: {t['schedule']}")
        st.markdown(f"**Estimated Price**: NT$ {t['price_per_cycle']:,} per cycle")
