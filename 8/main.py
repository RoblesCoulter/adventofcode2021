def parse_file(filename):
    with open(filename) as f:
        lines = [x for x in f.read().splitlines()]
        patterns_outputs_partitions = [x.split(" | ") for x in lines]
        return [SignalEntry(x[0].split(' '), x[1].split(' ')) for x in patterns_outputs_partitions]


class SignalEntry:
    def __init__(self, unique_patterns, output_values):
        unique_patterns.sort(key=len)
        self.unique_patterns = unique_patterns
        self.output_values = output_values

        self.analyze_unique_patterns()

    def has_one(self):
        return sum([1 for x in self.output_values if len(x) == 2])

    def has_four(self):
        return sum([1 for x in self.output_values if len(x) == 4])

    def has_seven(self):
        return sum([1 for x in self.output_values if len(x) == 3])

    def has_eight(self):
        return sum([1 for x in self.output_values if len(x) == 7])

    def calculate_1478(self):
        return self.has_one() + self.has_four() + self.has_seven() + self.has_eight()

    def analyze_unique_patterns(self):
        for pattern in self.unique_patterns:
            pattern_set = set([c for c in pattern])
            if(len(pattern) == 2):
                self.right_side = pattern_set
            elif(len(pattern) == 4):
                self.middle_upper_left = set(
                    [c for c in pattern]) - self.right_side
            elif(len(pattern) >= 5):
                break

    def decode_pattern(self, pattern):
        if(len(pattern) == 2):
            return '1'
        elif(len(pattern) == 3):
            return '7'
        elif(len(pattern) == 4):
            return '4'
        elif(len(pattern) == 5):
            pattern_set = set([c for c in pattern])

            if(self.middle_upper_left.issubset(pattern_set)):
                return '5'
            if(self.right_side.issubset(pattern_set)):
                return '3'
            else:
                return '2'
        elif(len(pattern) == 6):  # 0, 9, 6
            pattern_set = set([c for c in pattern])
            if(not self.middle_upper_left.issubset(pattern_set)):  # 0
                return '0'
            elif(self.right_side.issubset(pattern_set)):
                return '9'
            else:
                return '6'
        else:
            return '8'

    def decode_output(self):
        return int(''.join([self.decode_pattern(x) for x in self.output_values]))


def main():
    print("Part 1")
    entries = parse_file("input.txt")
    print(sum([x.calculate_1478() for x in entries]))
    print("Part 2")
    print(sum([x.decode_output() for x in entries]))


__name__ == "__main__" and main()
