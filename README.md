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

## 💬 Feedback & Contributions

We welcome contributions from the community!  
If you’d like to help improve this tool:

- 💡 **Feature Requests & Bug Reports**:  
  Please [create a new issue](https://github.com/syedacodes/sheetify/issues) describing the problem or idea.

- 🔧 **Pull Requests (PRs)**:  
  Fork this repository, make your changes in a feature branch, and open a pull request with a clear description.

Before submitting a PR, please make sure:
- Your code is clean and follows project conventions.
- You’ve tested your changes.
- The PR references an open issue if applicable.

We appreciate your support! 🙌