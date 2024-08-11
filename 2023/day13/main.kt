import kotlin.io.path.Path
import kotlin.io.path.readLines

typealias Puzzle = List<String>

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test 1 = ${solve(testInput())}")
    println("Part 1 = ${solve(input())}")
    println("Test 1 = ${solve(testInput(), maxDiff = 1)}")
    println("Part 2 = ${solve(input(), maxDiff = 1)}")
}

@Suppress("ExpressionBodySyntax")
private fun solve(input: List<String>, maxDiff: Int = 0): Int = input
    .toPuzzles()
    .sumOf { puzzle ->
        puzzle.findReflection(maxDiff) ?: 
            checkNotNull(puzzle.rotate90().findReflection(maxDiff)) * 100
    }


private fun Puzzle.findReflection(maxDiff: Int): Int? = first()
    .indices
    .find { index ->
        map { it.diffCount(index) ?: return@find false }
            .sumOf { it } == maxDiff
    }

fun String.diffCount(index: Int): Int? {
    if (index == 0) return null
    val (part1, part2) = subSequence(0, index) to subSequence(index, lastIndex + 1)

    return part1.reversed()
        .zip(part2)
        .count { it.first != it.second }
}

private fun List<String>.toPuzzles(): Sequence<Puzzle> {
    val puzzle = mutableListOf<String>()
    return sequence {
        forEach { line ->
            if (line.isBlank()) {
                yield(puzzle)
                puzzle.clear()
            } else {
                puzzle.add(line)
            }
        }
        yield(puzzle)
    }
}

private fun readInput(name: String) = Path("./", "$name.txt")
    .readLines()

fun List<String>.column(col: Int): String = indices
    .map { get(it)[col] }
    .joinToString(separator = "")

fun List<String>.rotate90(): List<String> = first().indices.map { index -> column(index) }
