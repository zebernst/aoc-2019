from pathlib import Path
from abc import ABC, abstractmethod

from solutions import *


def get_data(*, day: int):
    aoc_dir = Path(__file__).resolve().parent

    if not isinstance(day, int):
        print(f"{day} is not a number!")
        exit(1)

    try:
        with open(aoc_dir / "input" / f"{day:02d}.txt") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Couldn't load get_data for day {day}.")
        print(e)
        exit(1)


class AOCProblem(ABC):
    day = None

    def __init__(self):
        self.data = get_data(day=self.day)

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    @classmethod
    def run(cls):
        inst = cls()
        print(f"Day {inst.day}")
        print(f" ├╼ Part 1: {inst.part1()}")
        print(f" └╼ Part 2: {inst.part2()}")


if __name__ == '__main__':
    Day01.run()
    Day02.run()
