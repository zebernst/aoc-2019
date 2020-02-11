import aoc._

object AOCRunner extends App {
  val day = args.map(_.toInt).headOption getOrElse 2

  val puzzles = Map(
    1 -> day01.Day01,
    2 -> day02.Day02
  )

  run(day)

  def filename(day: Int) = f"input/$day%02d.txt"

  def run(day: Int): Unit = {
    puzzles.get(day) match {
      case None => println(s"Day $day has not yet been solved!")
      case Some(puzzle) =>
        val res = filename(day)
        val (out1, out2) = puzzle.solve(res)

        println(s"Day $day")
        println(s" ├╼ Part 1: $out1")
        println(s" └╼ Part 2: $out2")
    }
  }
}
