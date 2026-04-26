import streamlit as st
import tempfile
import os
import processor

st.title("Bank CSV Generator")
st.write("Upload the Employee Salaries Excel file to generate the Bank CSV.")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    if st.button("Generate Bank CSV"):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            output_path = processor.process(tmp_path)

            with open(output_path, "rb") as f:
                csv_data = f.read()

            os.unlink(tmp_path)
            os.unlink(output_path)

            output_filename = os.path.basename(output_path)
            st.success("Done! Your file is ready.")
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=output_filename,
                mime="text/csv"
            )

        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")