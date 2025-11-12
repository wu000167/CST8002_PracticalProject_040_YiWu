"""
<base_record.py>
Yi Wu (040787698)
Purpose:
    Defines the BaseRecord superclass for the Intertidal Bivalves dataset.
    This class is inherited by DetailedRecord and SummaryRecord to
    demonstrate Inheritance and Polymorphism (Part 3).
"""

class BaseRecord:
    """
    Represents a single record (row) from the dataset.
    Common attributes used by both SummaryRecord and DetailedRecord.
    """

    def __init__(self,
                 site_identification: str = "",
                 year: str = "",
                 transect: str = "",
                 quadrat: str = "",
                 species_common_name: str = "",
                 count: int | str = 0):
        """
        Initialize the BaseRecord with dataset columns.
        Default values prevent missing-argument errors.
        """
        self.site_identification = site_identification
        self.year = year
        self.transect = transect
        self.quadrat = quadrat
        self.species_common_name = species_common_name
        self.count = count

    def to_dict(self) -> dict:
        """Convert this record into a dictionary (for saving/export)."""
        return {
            "Site identification": self.site_identification,
            "Year": self.year,
            "Transect": self.transect,
            "Quadrat": self.quadrat,
            "Species Common Name": self.species_common_name,
            "Count": self.count
        }

    def display(self) -> str:
        """Default (can be overridden)."""
        return (
            f"Site: {self.site_identification} | Year: {self.year} | "
            f"Species: {self.species_common_name} | Count: {self.count}"
        )
