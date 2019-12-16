import sys
from pathlib import Path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No day provided!")
        exit(1)

    day = int(sys.argv[1])
    day_dir: Path = Path(__file__).resolve().parent / "solutions" / f"Day{day:02d}"

    problem: Path = day_dir / "readme.md"
    solution: Path = day_dir / "solution.py"
    init: Path = day_dir.parent / "__init__.py"

    problem.touch(exist_ok=True)

    if not solution.exists():
        with solution.open("w") as f:
            f.writelines(
                [
                    "from aoc import AOCProblem\n",
                    "\n",
                    "\n",
                    f"class Day{day:02d}(AOCProblem):\n",
                    f"    day = {day}\n",
                    "\n",
                    "    def preprocess(self, data):\n",
                    "        pass\n",
                    "\n",
                    "    def part1(self):\n",
                    "        pass\n",
                    "\n",
                    "    def part2(self):\n",
                    "        pass\n",
                    "\n",
                    "\n",
                    "if __name__ == '__main__':\n",
                    f"    Day{day:02d}().run()\n",
                ]
            )

    with init.open() as f:
        lines = [l for l in f.readlines()[:-1] if not l.isspace()]
        day_import = f"from .Day{day:02d}.solution import Day{day:02d}\n"
        if day_import not in lines:
            lines.append(day_import)
        lines.sort()

        explicit_exports = f"__all__ = {[line.split()[-1] for line in lines if not line.isspace()]}\n"

    with init.open("w") as f:
        f.writelines(lines)
        f.write("\n")
        f.write(explicit_exports)

    print(f"Scaffolded workspace for Day {day:02d}.")
