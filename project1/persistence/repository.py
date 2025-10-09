import csv, os, uuid

from model.record import IntertidalRecord, HEADER_TO_ATTR
from model.record import FIELD_YEAR, FIELD_SITE_ID 

def _is_french_header_row(row: dict) -> bool:
    return (row.get(FIELD_YEAR, "") == "Année"
            or row.get(FIELD_SITE_ID, "") == "Identification du site")

def read_records(csv_path: str, limit: int | None = 100) -> list[IntertidalRecord]:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    
    # Validate headers
    with open(csv_path, "r", encoding="cp1252", newline="") as f:
        reader = csv.DictReader(f)
        found = set(reader.fieldnames or [])
        missing = [h for h in HEADER_TO_ATTR.keys() if h not in found]
        if missing:
            raise ValueError("CSV missing required columns: " + str(missing))
    
    # Read records
    out, count = [], 0
    with open(csv_path, "r", encoding="cp1252", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if _is_french_header_row(row):
                continue
            out.append(IntertidalRecord.from_row(row))
            count += 1
            if limit is not None and count >= limit:
                break
    return out

# Write records to a new CSV file, returning the path to the file
def write_records_csv(records: list[IntertidalRecord], out_dir: str = "out") -> str:
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{uuid.uuid4()}.csv"
    out_path = os.path.join(out_dir, filename)

    headers = list(HEADER_TO_ATTR.keys())
    # Write CSV
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in records:
            writer.writerow(r.to_dict())
    return out_path