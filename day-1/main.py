def part1():
    total_fuel = 0
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            total_fuel = total_fuel + int(int(line) / 3) - 2
    return total_fuel


def calc_fuel(mass):
    if mass < 9:
        return 0
    else:
        fuel = int(mass / 3) - 2
        return fuel + calc_fuel(fuel)


def part2():
    total_fuel = 0
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            total_fuel = total_fuel + calc_fuel(int(line))
    return total_fuel


if __name__ == '__main__':
    print(part1())
    print(part2())






