import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(example.subtract(8, 2), 6)

    def test_multiply(self):
        self.assertEqual(example.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(example.divide(12, 6), 2)


if __name__ == '__main__':
    unittest.main()
