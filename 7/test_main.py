import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.positions = parse_file('input.txt')

    def test_file_loaded(self):
        self.assertEqual(len(self.positions), 1000)
        self.assertEqual(self.positions[0], 1101)
        self.assertEqual(self.positions[-1], 94)

    def test_part_1(self):
        self.assertEqual(analyze_crab_positions([1, 2, 3]), 2)
        self.assertEqual(analyze_crab_positions([1, 1, 1]), 0)
        self.assertEqual(analyze_crab_positions([1, 1, 3]), 2)

    def test_part_2(self):
        self.assertEqual(analyze_crab_positions([1, 2, 3, 1, 1, 1], False), 4)
        self.assertEqual(analyze_crab_positions([1, 1, 1, 5], False), 10)


__name__ == '__main__' and unittest.main()
