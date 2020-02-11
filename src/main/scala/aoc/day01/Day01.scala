package aoc.day01

import aoc.SimpleCommonPuzzle
import util.Files.read


object Day01 extends SimpleCommonPuzzle[Seq[Int], Int, Int] {
  override def parse(resource: String): Seq[Int] = read(resource).flatMap(e => e.toIntOption)

  override def part1(input: Seq[Int]): Int = input map calcFuel sum

  override def part2(input: Seq[Int]): Int = input map calcFuelComplete sum

  private def calcFuel(mass: Int) = mass / 3 - 2
  private def calcFuelComplete(mass: Int) =
    (LazyList unfold mass)(e => Some(calcFuel(e), calcFuel(e))) takeWhile (_ > 0) sum
}
