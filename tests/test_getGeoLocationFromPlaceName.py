import unittest

from app import getGeoLocationFromPlaceName

class TestStringMethods(unittest.TestCase):

    def test_londonLongLat(self):
        self.assertEqual(getGeoLocationFromPlaceName("Middlesbrough"), 'FOO')

if __name__ == '__main__':
    unittest.main()