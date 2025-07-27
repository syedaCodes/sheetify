# 📄 Sheetify

A no-code tool that allows users to import messy, unstructured data (CSV, text, or JSON), clean and organize it, and export it to Excel or Google Sheets.

## 🚀 Features (Planned)

- Upload or paste CSV, TXT, or JSON data
- Auto-detect and map fields
- Preview & edit tabular data
- Export as Excel (.xlsx) or to Google Sheets

## 📦 Tech Stack

- **Frontend**: Streamlit (for prototype)
- **Backend**: Python (FastAPI in future)
- **Data Handling**: pandas, openpyxl, json
- **Optional**: gspread for Google Sheets integration

## 📌 Project Roadmap

- [ ] Basic Streamlit UI
- [ ] Handle CSV/Delimited Text Input
- [ ] Add JSON support
- [ ] Excel export
- [ ] Google Sheets integration
- [ ] Saved templates (field mapping)

## 🛠️ Setup Instructions

```bash
git clone https://github.com/syedacodes/sheetify.git
cd sheetify
pip install -r requirements.txt
streamlit run app.py