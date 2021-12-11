def parse_file(file):
    call_order = []
    boards = []
    with open(file) as f:
        lines = f.read().splitlines()
        call_order = load_call_order(lines[0])
        boards = load_boards(lines[2:])
    return call_order, boards


def load_call_order(line):
    return [int(x) for x in line.split(',')]


def load_boards(lines):
    boards = []
    board = []
    for line in lines:
        if(line == ''):
            boards.append(board)
            board = []
        else:
            for num in line.split(" "):
                if(num != ''):
                    board.append(int(num))
    if(len(board) > 0):
        boards.append(board)
    return boards


class BingoGame:
    def __init__(self, call_order, boards, grid_size):
        self.call_order = call_order
        self.boards = [BingoBoard(board, grid_size) for board in boards]
        self.winners = 0
        print(sorted(call_order))

    def draw_number(self):
        number_drawn = self.call_order.pop(0)
        final_score = None
        for i, board in enumerate(self.boards):
            board.update_board(number_drawn)
            if(not board.won and board.bingo()):
                final_score = board.calculate_final_score(number_drawn)
                board.won = True
                print("Player {} wins with a score of {}".format(
                    i, final_score))
                self.winners += 1
                print("{} players have won, out of {} boards".format(
                    self.winners, len(self.boards)))

        return final_score


class BingoBoard:
    def __init__(self, board, grid_size):
        self.board = board
        self.grid_size = grid_size
        self.marked_board = [False] * grid_size * grid_size
        self.won = False

    def calculate_final_score(self, last_number):
        unmarked = [i for i, x in zip(self.board, self.marked_board) if not x]
        return sum(unmarked) * last_number

    def update_board(self, number):
        if(self.board.count(number) > 0):
            index = self.board.index(number)
            self.marked_board[index] = True

    def bingo(self):
        for i in range(0, self.grid_size):
            if((sum(self.marked_board[i::self.grid_size]) == self.grid_size) or (sum(self.marked_board[i*self.grid_size:(i*self.grid_size)+self.grid_size]) == self.grid_size)):
                return True
        return False


def main():
    print("Part 1")
    call_order, boards = parse_file('input.txt')
    game = BingoGame(call_order, boards, 5)
    while(game.call_order):
        draw = game.draw_number()
        if(draw is not None):
            print(draw)
            break

    print("Part 2")
    call_order, boards = parse_file('input.txt')
    game = BingoGame(call_order, boards, 5)

    while(game.call_order):
        draw = game.draw_number()


__name__ == '__main__' and main()
