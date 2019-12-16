from aoc import AOCProblem


class Day01(AOCProblem):
    day = 1

    def part1(self):
        modules = [int(m) for m in self.data.splitlines()]

        def calculate_fuel(module):
            return module // 3 - 2

        return sum(calculate_fuel(m) for m in modules)

    def part2(self):
        pass


if __name__ == '__main__':
    Day01().run()
