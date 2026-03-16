import unittest

from app import getGeoLocationFromPlaceName

class TestGeoLocator(unittest.TestCase):

    def checkLocationOfLondon(self):
        self.assertEqual(getGeoLocationFromPlaceName("London"), [51.5072, 0.1276])

if __name__ == '__main__':
    unittest.main()