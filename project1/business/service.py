"""
File: service.py
Course: CST8002 - Practical Project Part 3
Author: Yi Wu (040787698)

Purpose:
    Provides the business logic layer for handling records.
    Integrates Part 3's Inheritance & Polymorphism demonstration
    by generating subclassed record objects (DetailedRecord, SummaryRecord)
    and calling their display() method polymorphically.
"""
from typing import Optional
from model.record import IntertidalRecord, FIELD_SPECIES_COMMON, FIELD_COUNT
from persistence.repository import read_records, write_records_csv
from model.base_record import BaseRecord
from model.detailed_record import DetailedRecord
from model.summary_record import SummaryRecord


class RecordService:
    def __init__(self):
        self.records: list[IntertidalRecord] = []

    def load_from_csv(self, csv_path: str, limit: int | None = 100) -> int:
        """Load records from CSV."""
        self.records = read_records(csv_path, limit)
        return len(self.records)

    def reload_from_csv(self, csv_path: str, limit: int | None = 100) -> int:
        return self.load_from_csv(csv_path, limit)

    def list_all(self) -> list[IntertidalRecord]:
        return self.records

    def get(self, index: int) -> Optional[IntertidalRecord]:
        return self.records[index] if 0 <= index < len(self.records) else None

    def add(self, rec: IntertidalRecord) -> None:
        self.records.append(rec)

    def update(self, index: int, patch: dict) -> bool:
        rec = self.get(index)
        if not rec:
            return False
        for k, v in patch.items():
            setattr(rec, k, v)
        return True

    def delete(self, index: int) -> bool:
        if 0 <= index < len(self.records):
            self.records.pop(index)
            return True
        return False

    def export_csv(self, out_dir: str = "out") -> str:
        return write_records_csv(self.records, out_dir)

    # --------------------  Part 3 additions  --------------------
    def make_record(self, style: str, rec: IntertidalRecord) -> BaseRecord:
        """
        Factory method: converts an IntertidalRecord to a polymorphic subclass
        (DetailedRecord or SummaryRecord) based on style argument.
        """
        kwargs = {
            "site_identification": getattr(rec, "site_identification", ""),
            "year": getattr(rec, "year", ""),
            "transect": getattr(rec, "transect", ""),
            "quadrat": getattr(rec, "quadrat", ""),
            "species_common_name": getattr(rec, "species_common_name", ""),
            "count": getattr(rec, "count", ""),
}


        if style.lower() == "detailed":
            return DetailedRecord(**kwargs)
        return SummaryRecord(**kwargs)

    def format_records(self, style: str = "summary") -> list[str]:
        """
        Create and return a list of formatted strings demonstrating polymorphism.
        Each subclass overrides display(), so calling display() here will yield
        different output formats for Detailed vs Summary records.
        """
        formatted = []
        for rec in self.records:
            poly_obj = self.make_record(style, rec)
            formatted.append(poly_obj.display())  
        return formatted
