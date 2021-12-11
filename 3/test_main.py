import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self):
        with open("input.txt") as file:
            self.data = parse_file(file)

    def test_gamma_and_epsilon_start_empty(self):
        status_report = StatusReportParser()
        self.assertEqual(status_report.gamma_rate, 0)
        self.assertEqual(status_report.epsilon_rate, 0)

    def test_gamma_and_epsilon_parse_one_row(self):
        status_report = StatusReportParser()
        status_report.process_gamma_and_epsilon_rate(["011000110010"])
        self.assertEqual(status_report.gamma_rate, 1586)
        self.assertEqual(status_report.epsilon_rate, 2509)
        self.assertEqual(status_report.power_consumption(), 1586*2509)

    def test_gamma_and_epsilon_parse_multiple_rows(self):
        status_report = StatusReportParser()
        status_report.process_gamma_and_epsilon_rate(
            ["011000110010", "111011101000", "110100110010"])
        self.assertEqual(status_report.gamma_rate, 3634)
        self.assertEqual(status_report.epsilon_rate, 461)
        self.assertEqual(status_report.power_consumption(), 3634*461)

    # Part 2
    def test_oxygen_generator_rating_and_co2_scrubber_rating_starts_empty(self):
        status_report = StatusReportParser()
        self.assertEqual(status_report.oxygen_generator_rating, 0)
        self.assertEqual(status_report.co2_scrubber_rating, 0)

    def test_oxygen_generator_rating_and_co2_scrubber_rating_parse_one_row(self):
        status_report = StatusReportParser()
        status_report.process_oxygen_generator_and_co2_scrubber_rating(
            ["011000110010"])
        self.assertEqual(status_report.oxygen_generator_rating, 1586)
        self.assertEqual(status_report.co2_scrubber_rating, 1586)
        # self.assertEqual(status_report.power_consumption(), 1586*2509)

    def test_oxygen_generator_rating_and_co2_scrubber_rating_parse_two_rows(self):
        status_report = StatusReportParser()
        status_report.process_oxygen_generator_and_co2_scrubber_rating(
            ["011000110010", "111011101000"])
        self.assertEqual(status_report.oxygen_generator_rating, 3816)
        self.assertEqual(status_report.co2_scrubber_rating, 1586)
        # self.assertEqual(status_report.power_consumption(), 3634*461)

    def test_oxygen_generator_rating_and_co2_scrubber_rating_parse_multiple_rows(self):
        status_report = StatusReportParser()
        status_report.process_oxygen_generator_and_co2_scrubber_rating(
            ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"])
        self.assertEqual(status_report.oxygen_generator_rating, 23)
        self.assertEqual(status_report.co2_scrubber_rating, 10)


__name__ == "__main__" and unittest.main()
