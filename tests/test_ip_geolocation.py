# tests/test_ip_geolocation.py

import unittest
from src.modules.ip_geolocation import IPGeolocation

class TestIPGeolocation(unittest.TestCase):
    def test_get_geolocation(self):
        geolocation = IPGeolocation.get_geolocation("8.8.8.8")
        self.assertIsNotNone(geolocation)
        self.assertIn("ip", geolocation)
        self.assertEqual(geolocation["ip"], "8.8.8.8")

if __name__ == "__main__":
    unittest.main()

