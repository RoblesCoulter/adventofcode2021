def main():
    with open("input.txt") as file:
        data = parse_file(file)
        part1(data)
        part2(data)


def part1(data):
    print("Part 1")
    print("")
    print("")
    status_report = StatusReportParser()
    status_report.process_gamma_and_epsilon_rate(data)
    print(status_report.power_consumption())


def part2(data):
    print("Part 2")
    print("")
    print("")
    status_report = StatusReportParser()
    status_report.process_oxygen_generator_and_co2_scrubber_rating(data)
    print(status_report.life_support_rating())


def parse_file(file):
    return [row for row in file.read().splitlines()]


class StatusReportParser:
    def __init__(self):
        self.gamma_rate = 0
        self.epsilon_rate = 0
        self.oxygen_generator_rating = 0
        self.co2_scrubber_rating = 0

    # O(n**2) approach
    def process_gamma_and_epsilon_rate(self, data):
        ones_counter = [0] * 12
        zeros_counter = [0] * 12

        for row in data:
            for index, binary_code in enumerate(row):
                if(binary_code == "0"):
                    zeros_counter[index] += 1
                else:
                    ones_counter[index] += 1
        gamma, epsilon = self.calculate_rates(ones_counter, zeros_counter)
        self.gamma_rate = gamma
        self.epsilon_rate = epsilon

    def process_oxygen_generator_and_co2_scrubber_rating(self, data):
        self.process_oxygen_generator_rating(data)
        self.process_co2_scrubber_rating(data)

    def process_oxygen_generator_rating(self, data):
        ones_counter = 0
        filtered_data = data
        i = 0
        while(len(filtered_data) > 1):
            for row in filtered_data:
                if(row[i] == "1"):
                    ones_counter += 1
            zeros_counter = len(filtered_data) - ones_counter
            if(ones_counter >= zeros_counter):
                filtered_data = [row for row in filtered_data if row[i] == "1"]
            else:
                filtered_data = [row for row in filtered_data if row[i] == "0"]
            ones_counter = 0
            i += 1
        self.oxygen_generator_rating = self.binary_to_decimal(filtered_data[0])

    def process_co2_scrubber_rating(self, data):
        ones_counter = 0
        filtered_data = data
        i = 0
        while(len(filtered_data) > 1):
            for row in filtered_data:
                if(row[i] == "1"):
                    ones_counter += 1
            zeros_counter = len(filtered_data) - ones_counter
            if(zeros_counter <= ones_counter):
                filtered_data = [row for row in filtered_data if row[i] == "0"]
            else:
                filtered_data = [row for row in filtered_data if row[i] == "1"]
            i += 1
            ones_counter = 0
        self.co2_scrubber_rating = self.binary_to_decimal(filtered_data[0])

    def binary_to_decimal(self, binary_code):
        return int(binary_code, 2)

    def power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    def life_support_rating(self):
        return self.oxygen_generator_rating * self.co2_scrubber_rating

    def calculate_rates(self, ones_counter, zeros_counter):
        gamma = 0
        epsilon = 0
        for index, (one_count, zero_count) in enumerate(zip(ones_counter, zeros_counter)):
            if(one_count > zero_count):
                gamma += 2 ** (11 - index)
            else:
                epsilon += 2 ** (11 - index)

        return gamma, epsilon


__name__ == "__main__" and main()
