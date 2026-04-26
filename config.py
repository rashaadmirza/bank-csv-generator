from datetime import datetime

COMPANY_ACCOUNT_ID = "100093712"

def get_output_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"Bank_{timestamp}.csv"