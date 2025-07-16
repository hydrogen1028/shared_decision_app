from utils.pdf_export import create_pdf
import streamlit as st

def display_therapies(therapies):
    for t in therapies:
        st.subheader(t["name"])
        # ... display info ...

        if st.button(f"📄 Download PDF Summary for {t['name']}"):
            pdf_path = create_pdf(t)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name=f"{t['name'].replace(' ', '_')}_summary.pdf",
                    mime="application/pdf"
                )
