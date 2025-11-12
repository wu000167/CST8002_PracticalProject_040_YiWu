"""
< test_polymorphism.py>
Yi Wu (040787698)
Purpose:
    Unit test verifying that polymorphic display() methods
    of DetailedRecord and SummaryRecord work correctly.
"""
import pytest
from model.detailed_record import DetailedRecord
from model.summary_record import SummaryRecord


@pytest.fixture
def sample_data():
    """Provide reusable test data for records."""
    return {
        "species_common_name": "Pacific Littleneck Clam",
        "site": "Bamfield",
        "year": "2017",
        "abundance": "53"
    }


def test_summary_record_display(sample_data):
    """Test that SummaryRecord display() produces single-line format."""
    record = SummaryRecord(**sample_data)
    output = record.display()
    assert "Pacific Littleneck Clam" in output
    assert "Bamfield" in output
    assert "\n" not in output  # summary should be single-line


def test_detailed_record_display(sample_data):
    """Test that DetailedRecord display() produces multi-line format."""
    record = DetailedRecord(**sample_data)
    output = record.display()
    assert "Species Common Name" in output
    assert "Pacific Littleneck Clam" in output
    assert "\n" in output  # detailed should be multi-line
