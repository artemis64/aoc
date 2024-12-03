import scala.io.Source
import scala.collection.mutable.ArrayBuffer

def getInputOne(filename: String): ArrayBuffer[Int] = {
  val masses = ArrayBuffer[Int]()
  for (line <- Source.fromFile(filename).getLines) {
    println(line)
    masses += line.trim.toInt
  }
  return masses
}

def computeTheFuel(mass: Int, sum: Int): (Int, Int) = {
  printf("Mass %d, sum %d \n", mass / 3 - 2, sum)
  if (mass / 3 - 2 > 0) {
    return computeTheFuel(mass / 3 - 2, sum + (mass / 3 - 2))
  }
  return (0, sum)
}