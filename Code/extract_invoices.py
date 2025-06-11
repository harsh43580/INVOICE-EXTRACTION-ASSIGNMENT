import os
import pdfplumber
import pandas as pd

INPUT_DIR = "../Input/"
OUTPUT_FILE = "../Output/extracted_data.xlsx"

invoice_data = []

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_amazon_data(text, filename):
    lines = text.split('\n')
    invoice = {
        "Platform": "Amazon",
        "Invoice File": filename,
        "Invoice Number": None,
        "Order Number": None,
        "Order Date": None,
        "Invoice Date": None,
        "Buyer": None,
        "Items": [],
        "Total Amount": None
    }

    for line in lines:
        if "Invoice Number" in line:
            invoice["Invoice Number"] = line.split(":")[-1].strip()
        elif "Order Number" in line:
            invoice["Order Number"] = line.split(":")[-1].strip()
        elif "Order Date" in line:
            invoice["Order Date"] = line.split(":")[-1].strip()
        elif "Invoice Date" in line:
            invoice["Invoice Date"] = line.split(":")[-1].strip()
        elif "Billing Address" in line:
            idx = lines.index(line)
            invoice["Buyer"] = lines[idx + 1].strip()
        elif "TOTAL:" in line or "Grand Total" in line:
            invoice["Total Amount"] = line.split(":")[-1].strip("₹ ").replace(",", "")

    return invoice

def extract_flipkart_data(text, filename):
    lines = text.split('\n')
    invoice = {
        "Platform": "Flipkart",
        "Invoice File": filename,
        "Invoice Number": None,
        "Order Number": None,
        "Order Date": None,
        "Invoice Date": None,
        "Buyer": None,
        "Items": [],
        "Total Amount": None
    }

    for line in lines:
        if "Invoice Number" in line or "Tax Invoice #" in line:
            invoice["Invoice Number"] = line.split("#")[-1].strip()
        elif "Order ID" in line:
            invoice["Order Number"] = line.split(":")[-1].strip()
        elif "Order Date" in line:
            invoice["Order Date"] = line.split(":")[-1].strip()
        elif "Invoice Date" in line:
            invoice["Invoice Date"] = line.split(":")[-1].strip()
        elif "Billing Address" in line or "Bill To" in line:
            idx = lines.index(line)
            invoice["Buyer"] = lines[idx + 1].strip()
        elif "Grand Total" in line:
            invoice["Total Amount"] = line.split("₹")[-1].strip().replace(",", "")

    return invoice

def main():
    for file_name in os.listdir(INPUT_DIR):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(INPUT_DIR, file_name)
            text = extract_text_from_pdf(file_path)

            if "Amazon" in text or "Appario" in text:
                data = extract_amazon_data(text, file_name)
            elif "Flipkart" in text:
                data = extract_flipkart_data(text, file_name)
            else:
                continue

            invoice_data.append(data)

    df = pd.DataFrame(invoice_data)
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"✅ Extraction complete! Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
