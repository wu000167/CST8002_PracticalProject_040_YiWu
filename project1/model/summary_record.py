"""
<summary_record.py>
Yi Wu (040787698)
Purpose:
    Defines the SummaryRecord subclass that inherits from BaseRecord.
    It overrides the display() method to produce a compact, single-line
    representation for quick summaries.
"""
from .base_record import BaseRecord


class SummaryRecord(BaseRecord):
    """
    SummaryRecord extends BaseRecord.
    It overrides display() to provide a concise, single-line format.
    """

    def __init__(self,
                 site_identification: str = "",
                 year: str = "",
                 transect: str = "",
                 quadrat: str = "",
                 species_common_name: str = "",
                 count: int | str = 0):
        """
        Initialize a SummaryRecord object, inheriting basic fields from BaseRecord.
        Default values are provided for safe instantiation.
        """
        super().__init__(site_identification=site_identification,
                         year=year,
                         transect=transect,
                         quadrat=quadrat,
                         species_common_name=species_common_name,
                         count=count)

    def display(self) -> str:
        """
        Overridden display method providing a summarized representation.
        Displays fewer details than DetailedRecord.
        """
        return (f"[Summary] {self.species_common_name} "
                f"({self.year}) - Count: {self.count}")
