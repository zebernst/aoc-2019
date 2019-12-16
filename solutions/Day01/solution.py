from aoc import AOCProblem


def calculate_fuel(module):
    return module // 3 - 2


class Day01(AOCProblem):
    day = 1

    def part1(self):
        modules = [int(m) for m in self.data.splitlines()]

        return sum(calculate_fuel(m) for m in modules)

    def part2(self):
        modules = [int(m) for m in self.data.splitlines()]

        total = 0
        for mod in modules:
            subtotal = 0
            result = calculate_fuel(mod)
            while result > 0:
                subtotal += result
                result = calculate_fuel(result)
            total += subtotal

        return total


if __name__ == '__main__':
    Day01.run()
