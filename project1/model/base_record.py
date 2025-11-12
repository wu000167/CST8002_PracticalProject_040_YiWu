"""
<base_record.py>
Yi Wu (040787698)
Purpose:
    Defines the BaseRecord superclass for the Intertidal Bivalves dataset.
    This class will be inherited by DetailedRecord and SummaryRecord to
    demonstrate the advanced topic: Inheritance and Polymorphism.
"""
class BaseRecord:
    """
    BaseRecord represents a generic record in the dataset.
    It stores the common attributes shared by all record types.
    """

    def __init__(self,
                 species_common_name: str,
                 site: str,
                 year: str,
                 abundance: str):
        # === Dataset column names ===
        self.species_common_name = species_common_name
        self.site = site
        self.year = year
        self.abundance = abundance

    def to_dict(self) -> dict:
        """
        Converts this record to a dictionary, preserving dataset column names.
        """
        return {
            "species_common_name": self.species_common_name,
            "site": self.site,
            "year": self.year,
            "abundance": self.abundance
        }

    def display(self) -> str:
        """
        Default display method (will be overridden by subclasses).
        This is the polymorphic target method.
        """
        return (f"Species: {self.species_common_name}, "
                f"Site: {self.site}, "
                f"Year: {self.year}, "
                f"Abundance: {self.abundance}")

