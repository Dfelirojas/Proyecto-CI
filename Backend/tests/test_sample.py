import unittest
from logic import add

class TestBasic(unittest.TestCase):
    def test_add(self):
        result = add(2, 2)
        self.assertEqual(result, 4)
