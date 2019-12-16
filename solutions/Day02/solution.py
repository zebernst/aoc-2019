from aoc import AOCProblem
from operator import add, mul

opcodes = {
    1: add,
    2: mul,
}


class Day02(AOCProblem):
    day = 2

    def preprocess(self, data):
        return [int(i) for i in data.split(',')]

    def part1(self):
        intcode = self.data
        intcode[1] = 12
        intcode[2] = 2
        idx = 0
        while intcode[idx] != 99:
            opcode = intcode[idx]
            pos1 = intcode[idx+1]
            pos2 = intcode[idx+2]
            outpos = intcode[idx+3]

            val1 = intcode[pos1]
            val2 = intcode[pos2]

            result = opcodes.get(opcode)(val1, val2)
            intcode[outpos] = result
            idx += 4

        return intcode[0]

    def part2(self):
        pass


if __name__ == '__main__':
    Day02.run()
