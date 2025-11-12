"""
<detailed_record.py>
Yi Wu (040787698)
Purpose:
    Defines DetailedRecord subclass (inherits from BaseRecord),
    providing a multi-line detailed format.
"""
from .base_record import BaseRecord


class DetailedRecord(BaseRecord):
    """Detailed, multi-line format for complete info."""

    def __init__(self,
                 site_identification: str = "",
                 year: str = "",
                 transect: str = "",
                 quadrat: str = "",
                 species_common_name: str = "",
                 count: int | str = 0):
        super().__init__(site_identification=site_identification,
                         year=year,
                         transect=transect,
                         quadrat=quadrat,
                         species_common_name=species_common_name,
                         count=count)

    def display(self) -> str:
        """Multi-line format for detailed view."""
        return (
            "=== Detailed Record ===\n"
            f"Site identification: {self.site_identification}\n"
            f"Year: {self.year}\n"
            f"Transect: {self.transect}\n"
            f"Quadrat: {self.quadrat}\n"
            f"Species Common Name: {self.species_common_name}\n"
            f"Count: {self.count}\n"
            "------------------------"
        )
