"""
CST8002 Programming Language Research Project
project1 - record.py
Proof of concept
Lanuage: Python 3.11
Author: Yi Wu
Date: 2025-09-20

"""

import csv
import os
from record import IntertidalRecord, HEADER_TO_ATTR, FIELD_DATA_FIELD_EN, FIELD_DATA_VALUE
from shname import show_name_banner

# CSV placeholder file path
CSV_FILE = "pacific_rim_npr_coastalmarine_intertidal_bivalves_1997-2017_data_dictionary.csv"
RECORD_LIMIT = 6   # load first 6 rows to demonstrate

def validate_headers(fieldnames):
    """
    Make sure the CSV contains the required headers.
    This proves we used the correct dataset columns.
    """
    found = set(fieldnames or [])
    missing = [h for h in HEADER_TO_ATTR.keys() if h not in found]
    if missing:
        raise ValueError("CSV missing required columns: " + str(missing))


def load_records(csv_path, limit=None):
    """
    Open the CSV file and read the first 'limit' rows.
    Convert each row into an IntertidalRecord object.
    Store them in a Python list and return it.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError("Dataset not found: " + csv_path)

    records = []

    # First check the headers (the first row)
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        validate_headers(reader.fieldnames)

    # Then read and build objects
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            rec = IntertidalRecord.from_row(row)
            records.append(rec)
            count += 1
            if (limit is not None) and (count >= limit):
                break

    return records