import unittest
import sys

sys.path.insert(0, "../apis")

from apis import getGeoLocationFromPlaceName

class TestGeoLocator(unittest.TestCase):

    def checkLocationOfLondon(self):
        self.assertEqual(getGeoLocationFromPlaceName("London"), [51.5072, 0.1276])

if __name__ == '__main__':
    unittest.main()