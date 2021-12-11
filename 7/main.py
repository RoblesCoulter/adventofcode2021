
from collections import Counter


def parse_file(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(',')]


def main():
    positions = parse_file('input.txt')
    print(analyze_crab_positions(positions))
    print(analyze_crab_positions(positions, constant_rate=False))


def analyze_crab_positions(positions, constant_rate=True):
    fuel_consumption = None
    counter = Counter(positions)

    for current_position in counter.keys():
        tmp_fuel_consumption = 0
        for j in counter.keys():
            if(current_position != j):
                abs_diff = abs(current_position - j)
                if(constant_rate):
                    tmp_fuel_consumption += abs_diff * counter[j]
                else:
                    tmp_fuel_consumption += ((abs_diff **
                                             2 + abs_diff) / 2) * counter[j]
                if fuel_consumption is not None and tmp_fuel_consumption > fuel_consumption:
                    break
        if fuel_consumption is None or tmp_fuel_consumption < fuel_consumption:
            fuel_consumption = tmp_fuel_consumption
    return fuel_consumption


__name__ == '__main__' and main()
