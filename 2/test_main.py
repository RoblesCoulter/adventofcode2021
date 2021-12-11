import unittest
from main import *


class TestMain(unittest.TestCase):

    # Horizontal position, aim and depth both start at 0
    def test_position_depth_start_0(self):
        dive = Dive()
        self.assertEqual(dive.horizontal, 0)
        self.assertEqual(dive.depth, 0)
        self.assertEqual(dive.aim, 0)

    # Forward n adds n to your horizontal position AND increases depth by aim multiplied by n
    def test_forward_n(self):
        dive = Dive()
        dive.forward(5)
        self.assertEqual(dive.horizontal, 5)
        self.assertEqual(dive.depth, 0)

    # Down n adds n to your aim
    def test_down_n(self):
        dive = Dive()
        dive.down(5)
        self.assertEqual(dive.aim, 5)

    # Up n decreases your aim by n
    def test_up_n(self):
        dive = Dive()
        dive.up(2)
        self.assertEqual(dive.aim, -2)

    def test_final_position(self):
        dive = Dive()
        dive.down(3)
        dive.forward(5)

        self.assertEqual(dive.finalPosition(), 75)

    def test_process_planned_course(self):
        planned_course = ["forward 5", "down 5", "forward 8", "up 3"]
        dive = Dive()
        dive.process_planned_course(planned_course)
        self.assertEqual(dive.finalPosition(), 520)


__name__ == '__main__' and unittest.main()
