def part1():
    higher_measurements = 0

    with open('input.txt') as f:
        data = [int(line) for line in f.read().strip().split('\n')]
        for i, current in enumerate(data):
            if i != 0:
                previous = data[i-1]
                if(current > previous):
                    higher_measurements += 1
    print(higher_measurements)


def part2():
    higher_measurements = 0
    group_size = 3
    with open('input.txt') as f:
        data = [int(line) for line in f.read().strip().split('\n')]
        for i in range(0, len(data)):
            if i != 0:
                current = sum(data[i:i+group_size])
                previous = sum(data[i-1:i+group_size-1])
                print("Comparing " + str(current) + " to " + str(previous))
                if(int(current) > int(previous)):
                    higher_measurements += 1

    print(higher_measurements)


__name__ == '__main__' and (part1() and part2())
