import kotlin.io.path.Path
import kotlin.io.path.readLines
import kotlin.math.abs

data class Coords(
    val x: Long,
    val y: Long,
)

const val GALAXY = '#'

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test = ${part1(testInput())}")
    println("Part 1 = ${part1(input())}")
    println("Part 2 = ${part2(input())}")
}

private fun parse(space: List<String>, calculateShift: (Int) -> Long): List<Coords> = buildList {
    val emptyRows = space.indices.filterAllEmpty(space::row)
    val emptyColumns = space.first().indices.filterAllEmpty(space::column)
    var emptyRowsCount = 0
    for (row in space.indices) {
        if (row in emptyRows) {
            emptyRowsCount++
        } else {
            var emptyColumnsCount = 0
            for (col in space[row].indices) {
                if (space[row][col] == GALAXY) {
                    add(
                        Coords(
                            x = row + calculateShift(emptyRowsCount),
                            y = col + calculateShift(emptyColumnsCount)
                        )
                    )
                } else if (col in emptyColumns) {
                    emptyColumnsCount++
                }
            }
        }
    }
}

private fun part1(input: List<String>, shiftMultiplier: Int = 2) = solve(input, shiftMultiplier)

private fun part2(input: List<String>, shiftMultiplier: Int = 1_000_000) = solve(input, shiftMultiplier)


private fun solve(input: List<String>, shiftMultiplier: Int): Long {
    val galaxy = parse(input) { it * (shiftMultiplier.toLong() - 1) }
    return galaxy
        .pairs()
        .sumOf { (first: Coords, second: Coords) ->
            abs(first.x - second.x) + abs(first.y - second.y)
        }
}

@OptIn(ExperimentalStdlibApi::class)
private fun <T> List<T>.pairs(): Sequence<Pair<T, T>> = sequence {
    for (i in 0..<lastIndex) {
        for (j in i..lastIndex) {
            yield(get(i) to get(j))
        }
    }
}

private fun IntRange.filterAllEmpty(chars: (Int) -> Sequence<Char>): Set<Int> {
    return filterTo(mutableSetOf()) { i -> chars(i).all { it == '.' } }
}

private fun readInput(name: String) = Path("./", "$name.txt").readLines()

private fun List<String>.row(row: Int): Sequence<Char> = this[row].asSequence()

private fun List<String>.column(col: Int): Sequence<Char> = sequence {
    for (row in indices) yield(this@column[row][col])
}
