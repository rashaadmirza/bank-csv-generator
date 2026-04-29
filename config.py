from datetime import datetime
import os

def get_company_account_id():
    try:
        import streamlit as st
        return st.secrets["COMPANY_ACCOUNT_ID"]
    except Exception:
        return "100093712"

COMPANY_ACCOUNT_ID = get_company_account_id()

def get_output_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"Bank_{timestamp}.csv"