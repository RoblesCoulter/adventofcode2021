import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self):
        self.data = parse_file("input.txt")

    def test_file_is_loaded(self):
        self.assertEqual(len(self.data), 500)
        self.assertEqual(self.data[0][0], "644,38")
        self.assertEqual(self.data[0][1], "644,265")
        self.assertEqual(self.data[499][0], "219,934")
        self.assertEqual(self.data[499][1], "441,934")

    def test_one_coordinate_is_inserted(self):
        vents = HydrothermalVents()
        vents.insert_coordinate(["644,38", "644,265"])
        self.assertEqual(vents.analyze_overlaps(), 0)

    def test_two_coordinates_are_inserted(self):
        vents = HydrothermalVents()
        vents.insert_coordinate(["644,38", "644,265"])
        vents.insert_coordinate(["644,41", "644,43"])
        self.assertEqual(vents.analyze_overlaps(), 3)

    # Part 2
    def test_two_coordinates_are_inserted_and_diagonal(self):
        vents = HydrothermalVents()
        vents.insert_coordinate(["1,1", "3,3"], True)
        vents.insert_coordinate(["3,2", "3,5"], True)
        self.assertEqual(vents.analyze_overlaps(), 1)
        vents.insert_coordinate(["9,7", "7,9"], True)
        vents.insert_coordinate(["8,4", "8,9"], True)
        self.assertEqual(vents.analyze_overlaps(), 2)

        # def test_main(self):
        #     self.assertEqual(main(), None)
__name__ == '__main__' and unittest.main()
