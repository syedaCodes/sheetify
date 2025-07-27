# 📄 Sheetify

A no-code tool that allows users to import messy, unstructured data (CSV, TXT, or JSON), clean and organize it, and export it to Excel — no coding required.

## 🚀 Features

- ✅ Paste or upload JSON, CSV, TSV files
- ✅ Auto-detects structure and converts to a table
- ✅ Preview parsed data before exporting
- ✅ Export to Excel (.xlsx)
- ⏳ Google Sheets export (coming soon)
- ⏳ Saved templates for recurring data cleanup

## 📦 Tech Stack

- **Frontend**: Streamlit (for MVP prototype)
- **Backend**: Python (FastAPI planned)
- **Data Handling**: pandas, openpyxl, json

## 🛣️ Project Roadmap

### ✅ Version 1 – MVP (Streamlit)
- [x] Paste/upload CSV, TXT, or JSON
- [x] Parse and auto-normalize raw data
- [x] Filter and select columns
- [x] Export to Excel and CSV
- [x] Minimal UI with Streamlit

### 🚧 Version 2 – Full Tech Stack Migration
_Rebuilding Sheetify with full control over frontend/backend for extensibility._

- ⚛️ Frontend: React + TailwindCSS UI
- 🔧 Backend: FastAPI (Python) for data processing
- 📁 Rich file upload/download support
- 🎨 Modern UI with flexible layouts and themes
- 📊 Column mapping, templates, and saved presets
- 📤 Export to Excel and Google Sheets
- 🧪 Better testing, modularization, and deployment readiness

## 🛠️ Setup Instructions

```bash
git clone https://github.com/syedacodes/sheetify.git
cd sheetify
pip install -r requirements.txt
streamlit run app.py
```
## Note: This is the prototype version of Sheetify built with Streamlit.
I'm currently working on a more flexible and powerful version using React, TailwindCSS, and FastAPI.
