import scala.io.Source
import scala.collection.mutable.ArrayBuffer
@main
def main(): Unit = {
  val masses = getInputOne("/Users/annachejnovska/Documents/Code advent/aoc2019/Input/OnaA.txt")
  var sum = 0
  for (mass <- masses){
    val (a,b) = computeTheFuel(mass, 0)
    sum += b
    printf("partial sum %d \n", sum)
  }
  println(sum)
}