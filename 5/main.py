def main():
    print("Part 1")
    data = parse_file('input.txt')
    vents = HydrothermalVents()
    for line in data:
        vents.insert_coordinate(line)
    print(vents.analyze_overlaps())

    print("Part 2")
    vents_diagonal = HydrothermalVents()
    for line in data:
        vents_diagonal.insert_coordinate(line, include_diagonal=True)
    print(vents_diagonal.analyze_overlaps())


def parse_file(filename):
    data = []
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(' -> ') for line in lines]
    return data


class HydrothermalVents:

    def __init__(self):
        self.coordinates = {}

    def insert_coordinate(self, coordinate, include_diagonal=False):
        x1, y1 = coordinate[0].split(',')
        x2, y2 = coordinate[1].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        start = min(x1, x2)
        end = max(x1, x2)

        if(x1 == x2):
            start = min(y1, y2)
            end = max(y1, y2)
            for current_y in range(start, end+1):
                self.update_coordinate(x1, current_y)
        elif(y1 == y2):
            for current_x in range(start, end+1):
                self.update_coordinate(current_x, y1)
        elif(include_diagonal):
            end_y = y1
            start_y = y2
            direction = 1
            if(start == x1):
                start_y = y1
                end_y = y2
            if(start_y > end_y):
                direction = -1
            for (current_x, current_y) in zip(list(range(start, end+1)), list(range(start_y, end_y+direction, direction))):
                self.update_coordinate(current_x, current_y)

    def update_coordinate(self, x, y):
        self.coordinates[(x, y)] = self.has_coordinate((x, y))

    def analyze_overlaps(self):
        return list(self.coordinates.values()).count(True)

    def has_coordinate(self, coordinate):
        return coordinate in self.coordinates


__name__ == "__main__" and main()
