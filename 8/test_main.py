import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.signal_entries = parse_file('input.txt')

    def test_file_process_correctly(self):
        first_entry = SignalEntry(['gfeabcd', 'adecfb', 'gcedb', 'cef', 'efgdc',
                                   'decabg', 'cbfg', 'edfga', 'fdegcb', 'cf'], ['fc', 'faedg', 'fdage', 'fec'])

        self.assertEqual(
            self.signal_entries[0].unique_patterns, first_entry.unique_patterns)
        self.assertEqual(
            self.signal_entries[0].output_values, first_entry.output_values)
        last_entry = SignalEntry(['efgda', 'ac', 'acf', 'dfgbec', 'dfeac', 'edfbc',
                                 'ecfdgba', 'fceabd', 'bfdcga', 'aecb'], ['ecadfgb', 'abcedf', 'cefad', 'cabe'])
        self.assertEqual(
            self.signal_entries[-1].unique_patterns, last_entry.unique_patterns)
        self.assertEqual(
            self.signal_entries[-1].output_values, last_entry.output_values)

    def test_has_one_in_output(self):
        entry = SignalEntry(['gfeabcd', 'adecfb', 'gcedb', 'cef', 'efgdc',
                             'decabg', 'cbfg', 'edfga', 'fdegcb', 'cf'], ['fc', 'faedg', 'fdage', 'fec'])
        self.assertTrue(entry.has_one())

    def test_has_four_in_output(self):
        entry = SignalEntry(['efgda', 'ac', 'acf', 'dfgbec', 'dfeac', 'edfbc',
                             'ecfdgba', 'fceabd', 'bfdcga', 'aecb'], ['ecadfgb', 'abcedf', 'cefad', 'cabe'])
        self.assertTrue(entry.has_four())

    def test_has_seven_in_output(self):
        entry = SignalEntry(['gfeabcd', 'adecfb', 'gcedb', 'cef', 'efgdc',
                             'decabg', 'cbfg', 'edfga', 'fdegcb', 'cf'], ['fc', 'faedg', 'fdage', 'fec'])
        self.assertTrue(entry.has_seven())

    def test_has_eight_in_output(self):
        entry = SignalEntry(['efgda', 'ac', 'acf', 'dfgbec', 'dfeac', 'edfbc',
                             'ecfdgba', 'fceabd', 'bfdcga', 'aecb'], ['ecadfgb', 'abcedf', 'cefad', 'cabe'])
        self.assertTrue(entry.has_eight())

    # Part 2
    def test_unique_patterns_contain_one(self):
        entry = SignalEntry(['cf'], ['fc'])
        self.assertEqual(entry.right_side, {'c', 'f'})

    def test_unique_patterns_contain_four(self):
        entry = SignalEntry(['cf', 'fec', 'fcab'], [])
        self.assertEqual(entry.middle_upper_left, {'a', 'b'})

    def test_output_values_contain_one_seven_or_four(self):
        entry1 = SignalEntry(['cf', 'fec', 'fcab'], ['fc'])
        self.assertEqual(entry1.decode_pattern('fc'), '1')

        entry2 = SignalEntry(['cf', 'fec', 'fcab'], ['fec'])
        self.assertEqual(entry2.decode_pattern('fec'), '7')

        entry3 = SignalEntry(['cf', 'fec', 'fcab'], ['fcab'])
        self.assertEqual(entry3.decode_pattern('fcab'), '4')

    def test_output_values_contain_two_three_five(self):
        entry1 = SignalEntry(['cf', 'fac', 'fcdb'], ['acdeg'])
        self.assertEqual(entry1.decode_pattern('acdeg'), '2')

        entry2 = SignalEntry(['cf', 'fac', 'fcdb'], ['acdfg'])
        self.assertEqual(entry2.decode_pattern('acdfg'), '3')

        entry3 = SignalEntry(['cf', 'fac', 'fcdb'], ['abdfg'])
        self.assertEqual(entry3.decode_pattern('abdfg'), '5')

    def test_output_values_contain_zero_six_nine(self):
        entry1 = SignalEntry(['cf', 'fac', 'fcdb'], ['abcefg'])
        self.assertEqual(entry1.decode_pattern('abcefg'), '0')

        entry2 = SignalEntry(['cf', 'fac', 'fcdb'], ['abdefg'])
        self.assertEqual(entry2.decode_pattern('abdefg'), '6')

        entry3 = SignalEntry(['cf', 'fac', 'fcdb'], ['abcdfg'])
        self.assertEqual(entry3.decode_pattern('abcdfg'), '9')


__name__ == '__main__' and unittest.main()
