import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test 1 = ${part1(testInput())}")
    println("Part 1 = ${part1(input())}")
    println("Test 2 = ${part2(testInput())}")
    println("Part 2 = ${part2(input())}")
}

private fun part1(input: List<String>): Int = input.sumOf { algoritm(it) }

fun part2(input: List<String>): Int {
    val boxes = List(256) { mutableMapOf<String, Int>() }

    input
        .forEach { word ->
            if (word.contains('=')) {
                val (key, number) = word.split("=")
                val boxIndex = algoritm(key)
                boxes[boxIndex][key] = number.toInt()
            } else if (word.contains('-')) {
                val key = word.substringBefore('-')
                val boxIndex = algoritm(key)
                boxes[boxIndex].remove(key)
            }
        }

    return boxes
        .mapIndexed { index, box ->
            box.values.mapIndexed { indexBox, lens ->
                (index + 1) * (indexBox + 1) * lens
            }.sum()
        }
        .sum()
}

private fun algoritm(word: String): Int {
    var currentValue = 0
    word.forEach { symbol ->
        val resultValue = ((currentValue + symbol.code) * 17) % 256
        currentValue = resultValue
    }

    return currentValue
}

fun log(s: () -> String) {
    if (false) println(s.invoke())
}

private fun readInput(name: String): List<String> = Path("./", "$name.txt")
    .readLines()
    .first()
    .split(",")
