import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apis.apis import getGeoLocationFromPlaceName

class TestGetGeoLocationFromPlaceName(unittest.TestCase):

    def test_checkLocationOfLondon(self):
        self.assertEqual(getGeoLocationFromPlaceName("London"), [51.50853, -0.12574])

if __name__ == "__main__":
    unittest.main()