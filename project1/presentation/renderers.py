"""
<renderers>
Yi Wu (040787698)
Purpose:
    Provides display helper functions for the presentation layer.
    Demonstrates polymorphism by calling record.display() on BaseRecord
    references, without needing to know the specific subclass type.
"""
from typing import List
from model.base_record import BaseRecord


def render_records(records: List[BaseRecord]) -> str:
    """
    Render a list of BaseRecord objects polymorphically.
    Each record may be a DetailedRecord or SummaryRecord.
    The correct display() method is called automatically.
    """
    if not records:
        return "No records available to display."

    lines = [record.display() for record in records]
    return "\n".join(lines)


def render_header(title: str = "Polymorphic Display") -> None:
    """
    Print a header with the student's full name, visible in screenshots.
    """
    print("=" * 40)
    print(f"{title}")
    print("Program by Yi Wu - 040787698")
    print("=" * 40)