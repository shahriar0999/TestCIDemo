import unittest
from example import add, mul

class TestMathFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(43, 57), 100)

    def test_multi(self):
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(4, 10), 41)

if __name__ == "__main__":
    unittest.main()