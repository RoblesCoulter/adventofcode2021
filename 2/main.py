
class Dive:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def forward(self, n):
        self.horizontal += n
        self.depth += (self.aim * n)

    def down(self, n):
        self.aim += n

    def up(self, n):
        self.aim -= n

    def finalPosition(self):
        return self.depth * self.horizontal

    def process_planned_course(self, course):
        for move in course:
            (move_type, n) = move.split(' ')
            if move_type == 'forward':
                self.forward(int(n))
            elif move_type == 'down':
                self.down(int(n))
            elif move_type == 'up':
                self.up(int(n))
        return self.finalPosition()


def main():
    course = open('input.txt').read().splitlines()
    dive = Dive()
    print(dive.process_planned_course(course))


__name__ == '__main__' and main()
