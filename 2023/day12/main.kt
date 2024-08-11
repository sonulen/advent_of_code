import kotlin.io.path.Path
import kotlin.io.path.readLines
import kotlin.math.abs

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test = ${part1(testInput())}")
    // println("Part 1 = ${part1(input())}")
    // println("Part 2 = ${part2(input())}")
}

@Suppress("ExpressionBodySyntax")
private fun part1(input: List<String>): Int {
    return input.map { line ->
        val (pattern, rawNumbers) = line.split(" ")
        pattern to rawNumbers.split(",").map(String::toInt)
    }.sumOf { (pattern: String, numbers: List<Int>) ->
        val regex = Regex(
            numbers.joinToString(
                prefix = "(?=([?.]*",
                separator = "[.?]+?",
                postfix = "[?.]*$))"
            ) { number -> "[#?]{$number}" }
        )
        println("{$pattern}[$numbers] regex=$regex")

        regex.findAll(pattern)
            .map {
                it.groupValues[1].log { "-result value {$it}" }
            }
            .filter { result ->
                val isContain = pattern.replace(result, "")
                    .log { " Another part = $it" }
                    .contains("#")
                    .log { " verdict = ${!it}" }

                !isContain
            }
            .count()
    }
}

private fun <T: Any> T.log(function: (T) -> String): T = also {
    if (true) println(function.invoke(this))
}

private fun part2(input: List<String>) = 0

private fun readInput(name: String) = Path("./", "$name.txt").readLines()
