"""
File: menu.py
Course: CST8002 - Practical Project Part 3
Author: Yi Wu (040787698)

Purpose:
    Provides the text-based user interface (presentation layer).
    Integrates Part 3’s inheritance & polymorphism demonstration
    by allowing the user to choose polymorphic display modes.
"""
from util.shname import show_name_banner
from business.service import RecordService
from model.record import IntertidalRecord, FIELD_SPECIES_COMMON, FIELD_COUNT
from presentation.renderers import render_records, render_header

# Dataset path
DATA_PATH = "data/pacific_rim_npr_coastalmarine_intertidal_bivalves_clams_1997-2017_data.csv"


def _print_records(records: list[IntertidalRecord]):
    """Helper: print list of basic records in plain text."""
    for i, r in enumerate(records, start=1):
        print(f"[{i}] {FIELD_SPECIES_COMMON}: {r.species_common_name} | {FIELD_COUNT}: {r.count}")
        if i % 10 == 0:
            print("Program by Yi Wu")


def run():
    """Main menu loop."""
    svc = RecordService()
    show_name_banner("Yi Wu")

    # Initial load
    try:
        n = svc.load_from_csv(DATA_PATH, limit=100)
        print(f"Loaded {n} records.")
    except Exception as e:
        print("ERROR loading data:", e)

    while True:
        print("\n=== CST8002 Practical Project - Yi Wu (040787698) ===")
        print("1) Reload data from CSV")
        print("2) Export current data to new CSV (UUID filename)")
        print("3) Show one record")
        print("4) Show many records")
        print("5) Create a new record (in-memory)")
        print("6) Edit a record (in-memory)")
        print("7) Delete a record (in-memory)")
        print("8) Polymorphic Display (Summary)")
        print("9) Polymorphic Display (Detailed)")
        print("0) Exit")
        show_name_banner("Yi Wu")

        choice = input("Select: ").strip()

        # -------- Basic CRUD operations --------
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
            name = input(f"{FIELD_SPECIES_COMMON}: ").strip()
            cnt = input(f"{FIELD_COUNT}: ").strip()
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

        # -------- Part 3: Inheritance & Polymorphism --------
        elif choice == "8":
            render_header("Polymorphic Display - Summary Format")
            formatted = svc.format_records("summary")
            print(render_records(formatted))

        elif choice == "9":
            render_header("Polymorphic Display - Detailed Format")
            formatted = svc.format_records("detailed")
            print(render_records(formatted))

        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Invalid choice.")