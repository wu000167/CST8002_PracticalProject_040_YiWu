"""
<test_polymorphism.py>
Author: Yi Wu (040787698)

Purpose:
    Unit tests verifying the polymorphic behavior of SummaryRecord
    and DetailedRecord classes. Ensures that the display() methods
    produce distinct outputs as expected in single-line and multi-line formats.
"""

import pytest
from model.summary_record import SummaryRecord
from model.detailed_record import DetailedRecord


@pytest.fixture
def sample_data():
    """Provide reusable mock data for record testing."""
    return {
        "site_identification": "4",
        "year": "1997",
        "transect": "1.7",
        "quadrat": "-7.1",
        "species_common_name": "Butter Clam",
        "count": "5"
    }


def test_summary_record_display(sample_data):
    """Verify that SummaryRecord.display() returns a concise, single-line format."""
    record = SummaryRecord(**sample_data)
    output = record.display()

    # Content validation
    assert "Butter Clam" in output
    assert "(1997)" in output
    assert "Count: 5" in output

    # Format validation: no line breaks expected
    assert "\n" not in output


def test_detailed_record_display(sample_data):
    """Verify that DetailedRecord.display() returns a multi-line detailed format."""
    record = DetailedRecord(**sample_data)
    output = record.display()

    # Content validation
    assert "Butter Clam" in output
    assert "Site identification" in output
    assert "Year: 1997" in output
    assert "Count: 5" in output

    # Format validation: must contain line breaks
    assert "\n" in output


def test_polymorphism_behavior(sample_data):
    """Check polymorphism: both subclasses share display() name but produce different results."""
    summary_obj = SummaryRecord(**sample_data)
    detailed_obj = DetailedRecord(**sample_data)

    # Ensure different behavior while sharing the same method name
    assert summary_obj.display() != detailed_obj.display()
    assert isinstance(summary_obj, SummaryRecord)
    assert isinstance(detailed_obj, DetailedRecord)
