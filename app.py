import json
import textwrap
from io import BytesIO, StringIO

import pandas as pd
from pandas import json_normalize
import streamlit as st

# ---- Page Configuration ----
st.set_page_config(page_title="Sheetify - Data to Excel", layout="wide")

# ---- App Header ----
st.title("📄 Sheetify: Raw Data to Excel Converter")
st.caption(
    """
    🛠️ **Sheetify** helps you convert raw data into clean Excel or CSV files. 
    - Paste raw JSON or upload CSV/TSV to quickly convert.  
    - Upload Excel/CSV/TXT files to filter and export only what you need.  
    - Download your final output as .xlsx or .csv — no coding required!
    """
)

# ---- Helper: Parse JSON safely and return a DataFrame ----
def parse_json_data(text):
    try:
        cleaned = textwrap.dedent(text).strip()
        parsed_json = json.loads(cleaned)
        if isinstance(parsed_json, list):
            return json_normalize(parsed_json)
        elif isinstance(parsed_json, dict):
            return json_normalize([parsed_json])
        else:
            st.warning("Unsupported JSON format. Use a list or object.")
            return None
    except Exception as e:
        st.error(f"Invalid JSON: {e}")
        return None

# ---- Helper: Parse CSV/TSV safely and return a DataFrame ----
def parse_csv_data(text):
    try:
        return pd.read_csv(StringIO(text), sep=None, engine="python")
    except Exception as e:
        st.error(f"Invalid CSV/TSV: {e}")
        return None

# ---- Tabs ----
tab1, tab2 = st.tabs(["📝 Quick Paste or Upload", "📊 Upload & Filter"])

# ----------------------
# ---- Tab 1 Logic ----
# ----------------------
with tab1:
    st.subheader("📋 Convert Raw JSON or CSV/TSV into a Table and Export")

    # Choose input format: JSON or CSV/TSV
    paste_format = st.radio("Format of data:", ["JSON", "CSV/TSV"], horizontal=True)

    parsed_df = None

    # If JSON is selected, show paste field
    if paste_format == "JSON":
        raw_text = st.text_area(
            "Paste your raw JSON data here:",
            height=200,
            placeholder='[\n  {"id": 1, "name": "Alice"},\n  {"id": 2, "name": "Bob"}\n]'
        )
        # Parse JSON if text is provided
        if raw_text:
            parsed_df = parse_json_data(raw_text)

    # If CSV/TSV is selected, show file uploader
    elif paste_format == "CSV/TSV":
        uploaded_file_tab1 = st.file_uploader(
            "📎 Upload a CSV or TSV file:",
            type=["csv", "tsv"]
        )
        # Parse file if uploaded
        if uploaded_file_tab1:
            try:
                parsed_df = pd.read_csv(uploaded_file_tab1)
            except Exception as e:
                st.error(f"❌ Failed to read CSV: {e}")

    # Show preview if parsing succeeded
    if parsed_df is not None:
        st.success("✅ Data parsed successfully.")
        st.dataframe(parsed_df.head())

        # If the user used JSON and parsing succeeded, offer CSV download
        if paste_format == "JSON" and parsed_df is not None:
            csv_buffer = StringIO()
            parsed_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv_buffer.getvalue(),
                file_name="converted_data.csv",
                mime="text/csv"
            )

# ----------------------
# ---- Tab 2 Logic ----
# ----------------------
with tab2:
    st.subheader("📤 Upload CSV, TXT, or Excel Files to Filter and Export")

    parsed_df = None

    # Allow CSV, TXT, or Excel upload
    uploaded_file = st.file_uploader(
        "Upload a CSV, TXT or Excel file to filter and customize",
        type=["csv", "txt", "xlsx"]
    )

    if uploaded_file:
        try:
            # Detect file type and parse accordingly
            if uploaded_file.name.endswith((".csv", ".txt")):
                parsed_df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                parsed_df = pd.read_excel(uploaded_file, engine='openpyxl')
            st.success("✅ File uploaded successfully.")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    # If data is loaded, show filtering and export options
    if parsed_df is not None:
        st.subheader("🔍 Data Preview")

        selected_columns = st.multiselect(
            "✅ Select columns to include in export:",
            options=parsed_df.columns.tolist(),
            default=parsed_df.columns.tolist()
        )

        if not selected_columns:
            st.warning("⚠️ Please select at least one column to export.")
        else:
            filtered_df = parsed_df[selected_columns]

            st.markdown("### 🎯 Optional Filters for Selected Columns")

            def is_telephone_field(col_name, series):
                name_match = any(k in col_name.lower() for k in ["phone", "mobile", "contact", "whatsapp", "tel"])
                sample = series.dropna().astype(str).head(10).tolist()
                value_match = all(any(char.isdigit() for char in val) and len(val) >= 6 for val in sample)
                return name_match or value_match

            filters_to_apply = {}

            for col in selected_columns:
                if pd.api.types.is_numeric_dtype(filtered_df[col]) or is_telephone_field(col, filtered_df[col]):
                    continue

                apply_filter = st.checkbox(f"Filter `{col}`", key=f"filter_{col}")

                if apply_filter:
                    if filtered_df[col].dtype == "object":
                        filtered_df[col] = filtered_df[col].astype(str).str.strip().str.title()

                    unique_vals = sorted(filtered_df[col].dropna().unique().tolist())
                    selected_vals = st.multiselect(
                        f"→ Values for `{col}`",
                        options=unique_vals,
                        default=unique_vals,
                        key=f"multi_{col}"
                    )
                    filters_to_apply[col] = selected_vals

            for col, selected_vals in filters_to_apply.items():
                filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]

            st.dataframe(filtered_df)

            # ---- XLSX Download ----
            xlsx_buffer = BytesIO()
            with pd.ExcelWriter(xlsx_buffer, engine='openpyxl') as writer:
                filtered_df.to_excel(writer, index=False)
            xlsx_buffer.seek(0)

            st.download_button(
                label="📥 Download as XLSX",
                data=xlsx_buffer,
                file_name="filtered_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # ---- CSV Download ----
            csv_buffer = StringIO()
            filtered_df.to_csv(csv_buffer, index=False)

            st.download_button(
                label="📥 Download as CSV",
                data=csv_buffer.getvalue(),
                file_name="filtered_data.csv",
                mime="text/csv"
            )
    else:
        st.info("ℹ️ No data loaded. Please upload a file to begin filtering.")
