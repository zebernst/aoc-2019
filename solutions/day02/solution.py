from aoc import AOCProblem
from solutions.intcode import IntcodeComputer


class Day02(AOCProblem):
    day = 2

    def preprocess(self, data):
        return [int(i) for i in data.split(",")]

    def part1(self):
        comp = IntcodeComputer(self.data)
        comp.setup(noun=12, verb=2)
        return comp.run()

    def part2(self):
        for noun in range(100):
            for verb in range(100):
                comp = IntcodeComputer(self.data)
                comp.setup(noun, verb)
                result = comp.run()

                if result == 19690720:
                    return 100 * noun + verb


if __name__ == "__main__":
    Day02.run()
