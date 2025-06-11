# 🧾 Invoice Extraction Automation

This project automates the extraction of structured data from Amazon and Flipkart invoice PDFs and neatly outputs them into an Excel spreadsheet.

Perfect for:
- E-commerce invoice analysis
- Accounting data entry automation
- Tax or reimbursement workflows
- Looking cool in front of your boss 😎

---

## 📁 Project Structure

Invoice-Extraction-Assignment/
├── Input/ # Folder containing input PDF invoices
│ ├── amazon_invoice1.pdf
│ ├── amazon_invoice2.pdf
│ ├── flipkart_invoice1.pdf
│ └── flipkart_invoice2.pdf
│
├── Output/ # Folder where extracted_data.xlsx will be saved
│ └── extracted_data.xlsx
│
├── Code/ # Python script to run the extraction
│ └── extract_invoices.py
│
├── requirements.txt # Required Python libraries
└── README.md # You’re reading this!


---

## 🚀 How to Run This Project

### 🐍 1. Clone the Repo
```bash
git clone https://github.com/harsh43580/INVOICE-EXTRACTION-ASSIGNMENT.git
cd invoice-extractor

Create & Activate Virtual Environment
On Windows

python -m venv venv
venv\Scripts\activate

On macOS/Linux

python3 -m venv venv
source venv/bin/activate

Install Required Libraries
pip install -r requirements.txt

Run the Script
cd Code
python extract_invoices.py

What the Output Looks Like
| Platform | Invoice File           | Invoice Number | Order Number | Buyer    | Order Date | Invoice Date | Total Amount |
| -------- | ---------------------- | -------------- | ------------ | -------- | ---------- | ------------ | ------------ |
| Amazon   | amazon\_invoice1.pdf   | MAA4-631658    | 407-6400628  | Ruban    | 06.08.2019 | 06.08.2019   | 30990.00     |
| Flipkart | flipkart\_invoice1.pdf | FAFO8F24...    | OD42808399.. | Amit Roy | 13-05-2023 | 13-05-2023   | 34348.00     |

Technologies Used
Python 
pdfplumber – to extract text from PDF invoices
pandas – to structure data
openpyxl – to export Excel files

License
MIT License — go forth and automate.

Author
Made with caffeine and curly braces by Harsh


---

### ✅ How to Use It:
1. Copy this text and save it as `README.md` inside your root folder.
2. Run:

```bash
git add README.md
git commit -m "Add custom README"
git push origin main





