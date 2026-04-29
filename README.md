# Bank CSV Generator

A simple tool that converts an Employee Salaries Excel file into a bank salary transfer CSV file. Available as a desktop app, a local web app, and a hosted web app.

For questions or support, contact: mirza.ra@northeastern.edu

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

## Option 1: Hosted Web App (Recommended for end users)

Access the live web app here: [bank-csv.streamlit.app](bank-csv.streamlit.app)

1. Upload the Excel file
2. Click **Generate Bank CSV**
3. Download the output CSV

Note: Files are processed on Streamlit's cloud servers and not stored permanently.

---

## Option 2: Standalone Executable

No Python or installation required. Just double click and use.

1. Download `BankCSVGenerator.exe` from the [releases](https://github.com/rashaadmirza/bank-csv-generator/releases) section
2. Double click it -- the browser opens automatically
3. Upload the Excel file, click **Generate Bank CSV**, download the output

Data is processed locally on your machine and never sent anywhere.

---

## Option 3: Run Locally from Source

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

Create a `config.py` file in the project root (this file is not committed to GitHub):

```python
from datetime import datetime
import os

def get_company_account_id():
    try:
        import streamlit as st
        return st.secrets["COMPANY_ACCOUNT_ID"]
    except Exception:
        return os.environ.get("COMPANY_ACCOUNT_ID", "your_company_account_id_here")

COMPANY_ACCOUNT_ID = get_company_account_id()

def get_output_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"Bank_{timestamp}.csv"
```

For the Streamlit web app locally, also create `.streamlit/secrets.toml`:

```toml
COMPANY_ACCOUNT_ID = "your_company_account_id_here"
```

### Run the Tkinter Desktop App

```bash
python main.py
```

### Run the Flask Web App Locally

```bash
python flask_app.py
```

### Run the Streamlit Web App Locally

```bash
streamlit run app.py
```

---

## Project Structure

```
bank-csv-generator/
├── main.py              # Tkinter desktop GUI
├── app.py               # Streamlit web app
├── flask_app.py         # Flask local web app (used for .exe packaging)
├── processor.py         # Core processing logic (shared by all interfaces)
├── config.py            # Constants and secrets (local only, not committed)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # HTML UI for Flask app
└── .streamlit/
    └── secrets.toml     # Local secrets (not committed)
```

---

## Deployment (Streamlit Cloud)

The hosted web app is deployed on [Streamlit Cloud](https://streamlit.io/cloud). To deploy your own instance:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your GitHub account
3. Create a new app pointing to `app.py`
4. Add `COMPANY_ACCOUNT_ID` under **Settings > Secrets**

---

## Packaging as Executable (PyInstaller)

To rebuild the `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" --noconsole flask_app.py
```

The output will be in the `dist` folder. Rename as needed.

---

## Dependencies

- [pandas](https://pandas.pydata.org/) - Excel file processing
- [openpyxl](https://openpyxl.readthedocs.io/) - Excel file reading
- [streamlit](https://streamlit.io/) - Streamlit web app framework
- [flask](https://flask.palletsprojects.com/) - Flask local web app and executable