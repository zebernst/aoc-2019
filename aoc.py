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

    def run(self):
        print(f"Day {self.day}")
        print(f" ├╼ Part 1: {self.part1()}")
        print(f" └╼ Part 2: {self.part2()}")


if __name__ == '__main__':
    Day01().run()
