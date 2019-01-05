object Day1Part2 {
  def main(args: Array[String]): Unit = {
    val allLines = Source.fromFile(args[0]).getLines
    val allNumbers = allLines.map(_.toInt)
    val total = allNumbers.sum
    println(total)
  }
}