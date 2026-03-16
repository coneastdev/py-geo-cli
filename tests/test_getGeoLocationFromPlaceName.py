import unittest
import os
from pathlib import Path

os.chdir(Path.cwd().parent)
print(Path.cwd())
from app import getGeoLocationFromPlaceName

class TestGeoLocator(unittest.TestCase):

    def checkLocationOfLondon(self):
        self.assertEqual(getGeoLocationFromPlaceName("London"), [51.5072, 0.1276])

if __name__ == '__main__':
    unittest.main()