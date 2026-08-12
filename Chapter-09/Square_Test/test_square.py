import unittest
from square import square

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), 25)


if __name__ == "__main__":
    unittest.main()



"""
Output :

Ran 1 test in 0.001s

OK
"""


