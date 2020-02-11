package util

import scala.io.Source

object Files {
  def read(resource: String): Seq[String] = Source.fromResource(resource).getLines().toSeq
}
