"""
CST8002 Programming Language Research Project
project1 - record.py
Proof of concept
Lanuage: Python 3.11
Author: Yi Wu
Date: 2025-09-20

Module purpose:
    Define the RECORD class representing ONE row in the dataset.
    The source code reference the dataset's column names.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, List, Tuple

# Define constants for column names in the dataset
FIELD_SITE_ID = "Site identification"
FIELD_YEAR = "Year"
FIELD_TRANSECT = "Transect"
FIELD_QUADRAT = "Quadrat"
FIELD_SPECIES_COMMON = "Species Common Name"
FIELD_COUNT = "Count"

# Map ORIGINAL header -> simple Python attribute name (snake_case)
HEADER_TO_ATTR = {
    FIELD_SITE_ID:        "site_id",
    FIELD_YEAR:           "year",
    FIELD_TRANSECT:       "transect",
    FIELD_QUADRAT:        "quadrat",
    FIELD_SPECIES_COMMON: "species_common_name",
    FIELD_COUNT:          "count",
}

class IntertidalRecord:
    """
    Class representing to hold one row from the CSV.
    Each attribute stores one data item from that row.
    """

    def __init__(self,
                 site_id=None,
                 year=None,
                 transect=None,
                 quadrat=None,
                 species_common_name=None,
                 count=None):

        self.site_id = site_id
        self.year = year
        self.transect = transect
        self.quadrat = quadrat
        self.species_common_name = species_common_name
        self.count = count

    @classmethod
    def from_row(cls, row_dict: dict):
        """
        Create an IntertidalRecord from a csv.DictReader row (a dict).
        """
        kwargs = {}
        for header, attr in HEADER_TO_ATTR.items():
            value = row_dict.get(header)
            if isinstance(value, str):
                value = value.strip()
            kwargs[attr] = value
        return cls(**kwargs)

    def to_dict(self) -> dict:
        """Convert this record back to ORIGINAL CSV headers -> values."""
        inv = {v: k for k, v in HEADER_TO_ATTR.items()}
        return {
            inv["site_id"]: self.site_id,
            inv["year"]: self.year,
            inv["transect"]: self.transect,
            inv["quadrat"]: self.quadrat,
            inv["species_common_name"]: self.species_common_name,
            inv["count"]: self.count,
        }

    def __str__(self) -> str:
        """Human-friendly display when printing a single record."""
        return (
            f"{FIELD_SPECIES_COMMON}: {self.species_common_name}\n"
            f"{FIELD_COUNT}: {self.count}\n"
            f"{FIELD_YEAR}: {self.year}\n"
            f"{FIELD_SITE_ID}: {self.site_id}\n"
            f"{FIELD_TRANSECT}: {self.transect}\n"
            f"{FIELD_QUADRAT}: {self.quadrat}"
        )

    def __repr__(self) -> str:
        """Debug one-liner shown in lists etc."""
        return (
            "IntertidalRecord("
            f"{FIELD_SPECIES_COMMON}={self.species_common_name!r}, "
            f"{FIELD_COUNT}={self.count!r}, "
            f"{FIELD_YEAR}={self.year!r}, "
            f"{FIELD_SITE_ID}={self.site_id!r}, "
            f"{FIELD_TRANSECT}={self.transect!r}, "
            f"{FIELD_QUADRAT}={self.quadrat!r})"
        )
