import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apis.apis import getGeoLocationFromPlaceName, getWeatherDataFromHeadings

class TestGetGeoLocationFromPlaceName(unittest.TestCase):

    def test_checkLocationOfLondon(self):
        self.assertEqual(getGeoLocationFromPlaceName("London"), [51.50853, -0.12574])

    def test_checkLocationOfMiddlesbrough(self):
        self.assertEqual(getGeoLocationFromPlaceName("middlesbrough"), [54.57623, -1.23483])

class TestGetWeatherDataFromHeadings(unittest.TestCase):

    def test_checkResponseOfLondon(self):
        forecast = getWeatherDataFromHeadings(51.50853, -0.12574)
        self.assertTrue(forecast["timezone"] in ["GMT", "BST"])
    
    def test_checkResponseOfBerlin(self):
        forecast = getWeatherDataFromHeadings(52.52437, 13.41053)
        self.assertEqual(forecast["timezone"], "GMT")

if __name__ == "__main__":
    unittest.main()