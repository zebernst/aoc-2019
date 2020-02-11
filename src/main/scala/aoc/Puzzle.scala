package aoc

trait Puzzle[R, I1, I2, O1, O2] {
  def parse(resource: String): R

  def preprocess1(raw: R): I1
  def preprocess2(raw: R): I2

  def part1(input: I1): O1
  def part2(input: I2): O2

  def solve(resource: String): (O1, O2) = {
    val result1 = part1(preprocess1(parse(resource)))
    val result2 = part2(preprocess2(parse(resource)))
    (result1, result2)
  }
}

trait CommonPuzzle[R, I, O1, O2] extends Puzzle[R, I, I, O1, O2] {
  def preprocess(raw: R): I

  override def preprocess1(raw: R): I = preprocess(raw)
  override def preprocess2(raw: R): I = preprocess(raw)

  override def solve(resource: String): (O1, O2) = {
    val input = preprocess(parse(resource))
    (part1(input), part2(input))
  }
}

trait SimpleCommonPuzzle[I, O1, O2] extends CommonPuzzle[I, I, O1, O2] {
  override def preprocess(raw: I): I = raw
}
