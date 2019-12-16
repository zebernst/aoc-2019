class IntcodeComputer:
    def __init__(self, intcode: list):
        self.memory = intcode[:]

    def resolve(self, opcode):
        if opcode == 1:
            return self.add, 3
        elif opcode == 2:
            return self.multiply, 3

        elif opcode == 99:
            return None, 0
        else:
            exit(1)

    def add(self, param1, param2, param3):
        result = self.memory[param1] + self.memory[param2]
        self.memory[param3] = result

    def multiply(self, param1, param2, param3):
        result = self.memory[param1] * self.memory[param2]
        self.memory[param3] = result

    def setup(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

    def run(self):
        ptr = 0
        while True:
            action, num_params = self.resolve(self.memory[ptr])
            if action is None:
                break

            params = slice(ptr + 1, ptr + 1 + num_params)
            action(*self.memory[params])

            ptr += 1 + num_params

        return self.memory[0]
