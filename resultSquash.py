import pandas as pd
import os
from datetime import date
import sys
'''
WHAT THIS DOES:
takes all of the files in a directory that end with `.csv` and outputs a single `.xlsx` file squashing them all together.

PREREQS:
pip install pandas
pip install openpyxl

ARGUMENTS: pass a single word when invoking this script to append context to the file name. for example, passing in `python resultSquash.py alex` will make the fileName `squash-alex-2025-05-28.xlsx`.
'''

purpose = sys.argv[1] if len(sys.argv) > 1 else ""
iso_date = date.today().isoformat()
suffix = f"-{purpose}" if purpose else ""
output_excel = f"squash{suffix}-{iso_date}.xlsx"

tables = {}

for filename in os.listdir():
    if filename.lower().endswith(".csv"):
        sheet_name = os.path.splitext(filename)[0][:31]  # Excel limits sheet names to 31 chars
        file_path = filename
        try:
            df = pd.read_csv(file_path)
            tables[sheet_name] = df
        except Exception as e:
            print(f"Error reading {filename}: {e}")

with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    for sheet_name, df in tables.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"\n✅ Combined Excel file created at: {output_excel}")