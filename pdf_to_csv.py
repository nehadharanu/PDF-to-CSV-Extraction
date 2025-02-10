import pdfplumber
import pandas as pd

pdf_path = "NeetPG24R1.pdf"
csv_path = "NeetPG24R1.csv"

data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            data.extend(tables)

df = pd.DataFrame(data)
df.to_csv(csv_path, index = False, header=False)
