from util.shname import show_name_banner
from business.service import RecordService
from model.record import IntertidalRecord, FIELD_SPECIES_COMMON, FIELD_COUNT

DATA_PATH = "data/pacific_rim_npr_coastalmarine_intertidal_bivalves_clams_1997-2017_data.csv"

def _print_records(records: list[IntertidalRecord]):
    for i, r in enumerate(records, start=1):
        print(f"[{i}] {FIELD_SPECIES_COMMON}: {r.species_common_name} | {FIELD_COUNT}: {r.count}")
        if i % 10 == 0:
            print("Program by Yi Wu") 
def run():
    svc = RecordService()
    show_name_banner("Yi Wu")

    # Initial load
    try:
        n = svc.load_from_csv(DATA_PATH, limit=100)
        print(f"Loaded {n} records.")
    except Exception as e:
        print("ERROR loading data:", e)

    while True:
        print("\n=== Menu ===")
        print("1) Reload data from CSV")
        print("2) Export current data to new CSV (UUID filename)")
        print("3) Show one record")
        print("4) Show many records")
        print("5) Create a new record (in-memory)")
        print("6) Edit a record (in-memory)")
        print("7) Delete a record (in-memory)")
        print("0) Exit")
        show_name_banner("Yi Wu")

        choice = input("Select: ").strip()
        if choice == "1":
            try:
                print("Reloading...")
                print("Loaded", svc.reload_from_csv(DATA_PATH, limit=100), "records.")
            except Exception as e:
                print("ERROR:", e)

        elif choice == "2":
            outp = svc.export_csv()
            print("Exported to:", outp)

        elif choice == "3":
            idx = int(input("Index (1-based): ")) - 1
            rec = svc.get(idx)
            print(rec if rec else "Not found")

        elif choice == "4":
            _print_records(svc.list_all())

        elif choice == "5":
            # Input fields
            name = input(f"{FIELD_SPECIES_COMMON}: ").strip()
            cnt  = input(f"{FIELD_COUNT}: ").strip()
            svc.add(IntertidalRecord(species_common_name=name, count=cnt))
            print("Added.")

        elif choice == "6":
            idx = int(input("Index (1-based): ")) - 1
            new_cnt = input(f"New {FIELD_COUNT}: ").strip()
            ok = svc.update(idx, {"count": new_cnt})
            print("Updated." if ok else "Index invalid.")

        elif choice == "7":
            idx = int(input("Index (1-based): ")) - 1
            print("Deleted." if svc.delete(idx) else "Index invalid.")

        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Invalid choice.")