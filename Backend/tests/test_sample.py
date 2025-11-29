import unittest
import logic

class TestBasic(unittest.TestCase):
    def test_math(self):
        self.assertEqual(2 + 2, 4)

    def test_logic_exists(self):
        self.assertTrue(hasattr(logic, "__file__"))
