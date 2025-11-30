"""
File: chart_service.py
Course: CST8002 - Practical Project Part 4
Author: Yi Wu (040787698)

Purpose:
    Business logic for the Part 4 novel feature (Vertical Bar Chart).
    Prepares numeric data from existing IntertidalRecord objects so that
    the presentation layer can render a vertical bar chart.
"""

from typing import List, Tuple
from business.service import RecordService
from model.record import (
    HEADER_TO_ATTR,
    FIELD_YEAR,
    FIELD_TRANSECT,
    FIELD_QUADRAT,
    FIELD_COUNT,
)


# We will only offer columns that are numeric / numeric-like in the dataset.
NUMERIC_HEADERS = [
    FIELD_COUNT,
    FIELD_YEAR,
    FIELD_TRANSECT,
    FIELD_QUADRAT,
]


class ChartService:
    """
    Uses the already-loaded records from RecordService and prepares
    (labels, numeric values) for the chart.
    """

    def __init__(self, record_service: RecordService):
        self.record_service = record_service

    def get_available_numeric_headers(self) -> List[str]:
        """
        Return a list of dataset column names that the user can select
        for the vertical bar chart.
        """
        return NUMERIC_HEADERS

    def prepare_series(
        self, header_name: str, max_points: int
    ) -> Tuple[List[str], List[float]]:
        """
        Build x-axis labels and y-axis numeric values for the chart.

        Args:
            header_name: one of the NUMERIC_HEADERS strings
            max_points:  maximum number of records to include

        Returns:
            labels: ["1", "2", ...] for x-axis
            values: [float, float, ...] numeric values for y-axis
        """
        records = self.record_service.list_all()
        attr_name = HEADER_TO_ATTR.get(header_name)

        if attr_name is None:
            # Should not happen if we only pass known headers
            return [], []

        labels: List[str] = []
        values: List[float] = []

        for index, rec in enumerate(records):
            raw_value = getattr(rec, attr_name, None)

            try:
                num = float(raw_value)
            except (TypeError, ValueError):
                # Skip non-numeric or missing values
                continue

            labels.append(str(index + 1))
            values.append(num)

            if len(values) >= max_points:
                break

        return labels, values
