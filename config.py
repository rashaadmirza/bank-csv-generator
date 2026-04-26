from datetime import datetime
import streamlit as st

COMPANY_ACCOUNT_ID = st.secrets["COMPANY_ACCOUNT_ID"]

def get_output_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"Bank_{timestamp}.csv"