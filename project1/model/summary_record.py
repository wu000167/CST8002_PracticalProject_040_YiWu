"""
<summary_record.py>
Yi Wu (040787698)
Purpose:
    Defines the SummaryRecord subclass that inherits from BaseRecord.
    It overrides the display() method to produce a compact, single-line
    representation for quick summaries.
    Demonstrates polymorphism in contrast with DetailedRecord.
"""
from .base_record import BaseRecord


class SummaryRecord(BaseRecord):
    """
    SummaryRecord extends BaseRecord.
    It overrides display() to provide a concise, single-line format.
    """

    def display(self) -> str:
        """
        Overridden display method providing a summarized representation.
        """
        return (f"{self.species_common_name} @ {self.site} "
                f"({self.year}) - Abundance: {self.abundance}")
