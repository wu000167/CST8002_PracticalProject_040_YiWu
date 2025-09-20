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
FIELD_DATA_FIELD_EN = "Data_Field_EN_Champ_de_la_donnée"
FIELD_DATA_FIELD_FR = "Data_Field_FR_Champ_de_la_donnée"
FIELD_DATA_VALUE    = "Data_Value_Valeur_de_la_donnée"
FIELD_VALUE_DESC_EN = "Value_Description_EN_Description_de_la_valeur"
FIELD_VALUE_DESC_FR = "Value_Description_FR_Description_du_la_valeur"

# Map ORIGINAL header -> simple Python attribute name (snake_case)
HEADER_TO_ATTR = {
    FIELD_DATA_FIELD_EN: "data_field_en",
    FIELD_DATA_FIELD_FR: "data_field_fr",
    FIELD_DATA_VALUE:    "data_value",
    FIELD_VALUE_DESC_EN: "value_description_en",
    FIELD_VALUE_DESC_FR: "value_description_fr",
}

class IntertidalRecord:
    """
    Class representing to hold one row from the CSV.
    Each attribute stores one data item from that row.
    """

    def __init__(self,
                 data_field_en=None,
                 data_field_fr=None,
                 data_value=None,
                 value_description_en=None,
                 value_description_fr=None):

        self.data_field_en = data_field_en
        self.data_field_fr = data_field_fr
        self.data_value = data_value
        self.value_description_en = value_description_en
        self.value_description_fr = value_description_fr

    @classmethod
    def from_row(cls, row_dict):
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