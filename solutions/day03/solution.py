from aoc import AOCProblem
from itertools import combinations


def parse(instruction: str):
    dir = instruction[0]
    amt = int(instruction[1:])

    modifier = -1 if dir in ("D", "L") else 1

    if dir in ("D", "U"):
        return 1, amt * modifier
    elif dir in ("L", "R"):
        return 0, amt * modifier


def alignment(segment: list):
    p1, p2 = segment
    if p2[1] - p1[1] == 0 and p2[0] - p1[0] != 0:
        return "h"
    elif p2[0] - p1[0] == 0 and p2[1] - p1[1] != 0:
        return "v"
    else:
        print("line is not horizontal or vertical")
        exit(1)


def intersection(seg1: tuple, seg2: tuple):
    seg1 = sorted(seg1)
    seg2 = sorted(seg2)
    if alignment(seg1) == alignment(seg2):
        return None

    if alignment(seg1) == "h":
        if seg1[0][0] <= seg2[0][0] <= seg1[1][0] and seg2[0][1] <= seg1[0][1] <= seg2[1][1]:
            return seg2[0][0], seg1[0][1]
    else:
        if seg1[0][1] <= seg2[0][1] <= seg1[1][1] and seg2[0][0] <= seg1[0][0] <= seg2[1][0]:
            return seg1[0][0], seg2[0][1]


def manhattan_dist(point: tuple):
    a, b = point
    return abs(a) + abs(b)


class Day03(AOCProblem):
    day = 3

    def preprocess(self, data: str):
        return [line.split(",") for line in data.splitlines()]

    def part1(self):
        paths = []
        for path in self.data:
            segments = [[0, 0]]
            for seg in path:
                prev = segments[-1]
                this = prev[:]
                idx, amt = parse(seg)
                this[idx] += amt
                segments.append(this)
            paths.append(segments)

        intersections = []
        distances = []
        for a, b in combinations(paths, r=2):
            for i, a1 in enumerate(a[:-1]):
                a2 = a[i+1]
                for j, b1 in enumerate(b[:-1]):
                    b2 = b[j+1]

                    if point := intersection((a1, a2), (b1, b2)) is not None:
                        intersections.append(point)
                        distances.append(manhattan_dist(point))

        return min(distances)

    def part2(self):
        pass


if __name__ == '__main__':
    Day03().run()
