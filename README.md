# Bank CSV Generator

A simple tool that converts an Employee Salaries Excel file into a bank salary transfer CSV file. Available as both a desktop app and a web app.

---

## What It Does

Takes an Excel file with employee salary data and generates a formatted CSV ready for bank salary transfers. Employees with a zero salary are automatically excluded. The output file is timestamped for easy tracking.

**Input:** `Employee_Salaries.xlsx` with columns: `IBAN`, `Salary`, `ID`, `Employee Name`

**Output:** `Bank_YYYYMMDDHHMMSS.csv` structured as:

```
HDR,,,,,
DTL,<company_id>,<IBAN>,<Salary>,<ID>,<Employee Name>
...
TRL,,,,,
```

---

## Web App

Access the live web app here: [bank-csv-generator.streamlit.app](https://bank-csv-generator.streamlit.app)

1. Upload the Excel file
2. Click **Generate Bank CSV**
3. Download the output CSV

---

## Local Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/rashaadmirza/bank-csv-generator.git
cd bank-csv-generator
pip install -r requirements.txt
```

### Configuration

Create a `config.py` file in the project root:

```python
from datetime import datetime
import streamlit as st

COMPANY_ACCOUNT_ID = "your_company_account_id_here"

def get_output_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"Bank_{timestamp}.csv"
```

For the Streamlit web app locally, also create `.streamlit/secrets.toml`:

```toml
COMPANY_ACCOUNT_ID = "your_company_account_id_here"
```

### Run the Desktop App

```bash
python main.py
```

### Run the Web App Locally

```bash
streamlit run app.py
```

---

## Project Structure

```
bank-csv-generator/
├── main.py              # Tkinter desktop GUI
├── app.py               # Streamlit web app
├── processor.py         # Core processing logic
├── config.py            # Constants and secrets (local only, not committed)
├── config.example.py    # Template for config.py
├── requirements.txt     # Python dependencies
└── .streamlit/
    └── secrets.toml     # Local secrets (not committed)
```

---

## Deployment

The web app is deployed on [Streamlit Cloud](https://streamlit.io/cloud). To deploy your own instance:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your GitHub account
3. Create a new app pointing to `app.py`
4. Add `COMPANY_ACCOUNT_ID` under **Settings > Secrets**

---

## Dependencies

- [pandas](https://pandas.pydata.org/) - Excel file processing
- [openpyxl](https://openpyxl.readthedocs.io/) - Excel file reading
- [streamlit](https://streamlit.io/) - Web app framework
