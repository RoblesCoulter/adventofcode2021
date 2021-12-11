import unittest
from main import *


class TestMain(unittest.TestCase):
    def setUp(self):
        call_order, boards = parse_file("input.txt")
        self.call_order = call_order
        self.boards = boards

    def test_file_is_loaded(self):
        self.assertEqual(self.call_order[0], 14)
        self.assertEqual(self.call_order[-1], 52)
        self.assertEqual(self.boards[0][0], 13)
        self.assertEqual(self.boards[0][-1], 19)
        self.assertEqual(self.boards[-1][0], 26)
        self.assertEqual(self.boards[-1][-1], 53)

    def test_bingo_starts_with_call_order_and_boards(self):
        call_order = [1, 2, 3, 4]
        boards = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 1, 9, 8, 7]]
        bingo = BingoGame(call_order=call_order, boards=boards, grid_size=3)
        self.assertEqual(len(bingo.call_order), 4)
        self.assertEqual(len(bingo.boards), 2)

    def test_bingo_draws_one_number_from_call_order_number_removed(self):
        bingo = BingoGame(call_order=[1], boards=[
                          [1, 2, 3, 4], [5, 6, 7, 8]], grid_size=2)
        self.assertEqual(bingo.draw_number(), None)
        self.assertEqual(len(bingo.call_order), 0)

    def test_bingo_draws_one_number_and_boards_updated(self):
        bingo = BingoGame(call_order=[1], boards=[
                          [1, 2, 3, 4], [5, 6, 7, 8]], grid_size=2)
        self.assertFalse(bingo.boards[0].bingo())
        self.assertFalse(bingo.boards[1].bingo())
        self.assertEqual(sum(bingo.boards[0].marked_board), 0)
        self.assertEqual(sum(bingo.boards[1].marked_board), 0)
        bingo.draw_number()
        self.assertEqual(sum(bingo.boards[0].marked_board), 1)
        self.assertEqual(sum(bingo.boards[1].marked_board), 0)

    def test_bingo_draws_two_numbers_first_board_wins_horizontal(self):
        bingo = BingoGame(call_order=[1, 2], boards=[
                          [1, 2, 3, 4], [5, 6, 7, 8]], grid_size=2)
        self.assertEqual(bingo.draw_number(), None)
        self.assertEqual(bingo.draw_number(), (3+4) * 2)

    def test_bingo_draws_two_numbers_second_board_wins_horizontal(self):
        bingo = BingoGame(call_order=[5, 6], boards=[
            [1, 2, 3, 4], [5, 6, 7, 8]], grid_size=2)
        bingo.draw_number()
        self.assertEqual(bingo.draw_number(), (7+8) * 6)

    def test_bingo_draws_two_numbers_first_board_wins_vertical(self):
        bingo = BingoGame(call_order=[1, 3], boards=[
            [1, 2, 3, 4], [5, 6, 7, 8]], grid_size=2)
        bingo.draw_number()
        self.assertEqual(bingo.draw_number(), (2+4) * 3)


__name__ == "__main__" and unittest.main()
