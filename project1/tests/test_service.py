import unittest
from business.service import RecordService
from model.record import IntertidalRecord

class TestRecordService(unittest.TestCase):
    def test_add_record(self):
        svc = RecordService()
        self.assertEqual(len(svc.list_all()), 0)
        svc.add(IntertidalRecord(species_common_name="Test Clam", count="3"))
        self.assertEqual(len(svc.list_all()), 1)
        self.assertEqual(svc.list_all()[0].species_common_name, "Test Clam")

if __name__ == "__main__":
    unittest.main()
