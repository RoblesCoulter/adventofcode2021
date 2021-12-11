from collections import Counter


def main():
    print("Part 1")
    sample = parse_file("input.txt")
    simulation = simulate_lanternfish_spawn(sample, 80)
    print(sum(simulation.values()))
    print("Part 2")
    simulation256 = simulate_lanternfish_spawn(sample, 256)
    print(sum(simulation256.values()))


def parse_file(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split(",")]


def simulate_lanternfish_spawn(sample, days):
    sample_map = Counter(sample)
    for day in range(days):
        day_updated_sample = Counter()
        for key in sample_map:
            num_fishes = sample_map[key]
            if key == 0:
                day_updated_sample[6] = num_fishes + day_updated_sample[6]
                day_updated_sample[8] = num_fishes + day_updated_sample[8]
            else:
                day_updated_sample[key - 1] = num_fishes + \
                    day_updated_sample[key - 1]
        sample_map = day_updated_sample
    return sample_map


__name__ == "__main__" and main()
