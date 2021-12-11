import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self):
        self.fish_sample = parse_file('input.txt')

    def test_file_loaded(self):
        self.assertEqual(len(self.fish_sample), 300)
        self.assertEqual(self.fish_sample[0], 3)
        self.assertEqual(self.fish_sample[-1], 4)

    # Part 1
    def test_lanternfish_spawns_new_fish_with_internal_timer_of_eight(self):
        sample = [0]
        days = 1
        spawn = simulate_lanternfish_spawn(sample, days)
        self.assertEqual(spawn, {6: 1, 8: 1})

    def test_lanternfish_internal_timer_lowers_after_two_days(self):
        sample = [5]
        days = 2
        spawn = simulate_lanternfish_spawn(sample, days)
        self.assertEqual(spawn, {3: 1})


__name__ == '__main__' and unittest.main()
