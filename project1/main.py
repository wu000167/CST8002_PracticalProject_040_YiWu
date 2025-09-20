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
    with open(csv_path, "r", encoding="cp1252", newline="") as f:
        reader = csv.DictReader(f)
        validate_headers(reader.fieldnames)

    # Then read and build objects
    with open(csv_path, "r", encoding="cp1252", newline="") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            rec = IntertidalRecord.from_row(row)
            records.append(rec)
            count += 1
            if (limit is not None) and (count >= limit):
                break

    return records

def print_records(records):
    """
    Loop over the list and print some fields.
    We show ORIGINAL header names in the text so it is very clear.
    """
    i = 1
    for r in records:
        print("[" + str(i) + "] "
              + FIELD_DATA_FIELD_EN + ": " + str(r.data_field_en)
              + " | "
              + FIELD_DATA_VALUE + ": " + str(r.data_value))
        i += 1

def main():
    #show banner
    show_name_banner("Yi Wu")

    #load records
    try:
        items = load_records(CSV_FILE, limit=RECORD_LIMIT)
    except FileNotFoundError as e:
        print("ERROR:", e)
        print("Tip: put the CSV next to main.py or change CSV_FILE in the code.")
        return
    except ValueError as e:
        print("ERROR:", e)
        print("Tip: check the header names in record.py and your CSV file.")
        return

    print_records(items)


if __name__ == "__main__":
    main()
