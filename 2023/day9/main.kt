import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test = ${part1(testInput())}")
    println("Part 1 = ${part1(input())}")
    println("Part 2 = ${part2(input())}")
}

private fun part1(input: List<List<Long>>): Long = input.sumOf { values ->
    produceDiffs(values).sumOf { it.last() }
}

private fun part2(input: List<List<Long>>): Long = input.sumOf { values ->
    produceDiffs(values).map { it.first() }.toList().reduceRight(Long::minus)
}

private fun produceDiffs(values: List<Long>): Sequence<List<Long>> {
    return generateSequence(values) { currentValues ->
        if (currentValues.any { it != 0L }) {
            currentValues.windowed(2) { (left, right) -> right - left }
        } else {
            null
        }
    }
}

private fun readInput(name: String) 
    = Path("./", "$name.txt")
        .readLines()
        .map { it.split(" ").map(String::toLong) }

