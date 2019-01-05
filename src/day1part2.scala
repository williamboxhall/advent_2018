


with open(sys.argv[1]) as input:
	deltas = map(int, input.readlines())
	frequency = 0
	seen = set()

	for delta in itertools.cycle(deltas):
		frequency += delta
		if frequency in seen:
			print frequency
			break
		else:
			seen.add(frequency)
	

object Day1Part2 {
  def main(args: Array[String]): Unit = {
    val deltas = Source.fromFile(args[0]).getLines.map(_.toInt)
  }
}