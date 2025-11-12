"""
<detailed_record.py>
Yi Wu (040787698)
Purpose:
    Defines the DetailedRecord subclass, which inherits from BaseRecord.
    It overrides the display() method to provide a verbose multi-line
    representation of the dataset record.
    This demonstrates method overriding (polymorphism).
"""
from .base_record import BaseRecord


class DetailedRecord(BaseRecord):
    """
    DetailedRecord extends BaseRecord.
    It overrides display() to present a detailed, multi-line output format.
    """

    def display(self) -> str:
        """
        Overridden display method providing a detailed representation.
        """
        return (
            "=== Detailed Record ===\n"
            f"Species Common Name: {self.species_common_name}\n"
            f"Site: {self.site}\n"
            f"Year: {self.year}\n"
            f"Abundance: {self.abundance}\n"
        )


