import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hanoi import move

class HanoiTestCase(unittest.TestCase):
    def test_hanoi(self):
        self.assertEqual(move(1, 'A', 'B', 'C'), 1)
        self.assertEqual(move(2, 'A', 'B', 'C'), 3)
        self.assertEqual(move(3, 'A', 'B', 'C'), 7)

if __name__ == '__main__':
    unittest.main()
