import kotlin.io.path.Path
import kotlin.io.path.readLines

typealias Field = List<CharArray>

enum class Direction {
    NORTH, SOUTH, EAST, WEST
}

const val ROCK = 'O'
const val BLOCK = '#'
const val EMPTY = '.'

fun main() {
    fun testInput() = readInput("test")
    fun input() = readInput("input")

    println("Test 1 = ${part1(testInput())}")
    // println("Part 1 = ${part1(input())}")
    println("Test 2 = ${part2(testInput())}")
    // println("Part 2 = ${part2(input())}")
}

private fun part1(input: Field): Int = input
    .apply { transform(Direction.NORTH) }
    .reversed()
    .mapIndexed { index, row ->
        row.count { it == ROCK } * (index + 1)
    }
    .sumOf { it }

private fun part2(input: Field): Int {
    repeat(1_000_000_000) {
        if (it % 1_000_000 == 0) println("iteration $it")
        input.transform(Direction.NORTH)
        input.transform(Direction.WEST)
        input.transform(Direction.SOUTH)
        input.transform(Direction.EAST)
    }

    return input
        .reversed()
        .mapIndexed { index, row ->
            row.count { it == ROCK } * (index + 1)
        }
        .sumOf { it }
}

@Suppress("LoopWithTooManyJumpStatements")
private fun Field.transform(direction: Direction) {
    val iterateOnX = when(direction) {
        Direction.NORTH -> first().indices
        Direction.SOUTH -> first().indices.reversed()
        Direction.EAST ->  indices
        Direction.WEST -> indices.reversed()
    }

    val iterateOnY = when(direction) {
        Direction.NORTH -> indices
        Direction.SOUTH -> indices.reversed()
        Direction.EAST ->  first().indices
        Direction.WEST -> first().indices.reversed()
    }

    log { "Field: \n ${this.map { "-- ${it.map { it }}\n" }}" }
    log { "- iterateOnX: $iterateOnX \n iterateOnY: $iterateOnY" }

    for (x in iterateOnX) {
        for (y in iterateOnY) {
            if (y == iterateOnY.first) {
                set(x,y, get(x,y))
                continue
            }
            val current = get(x,y)
            log { "--- Current [$x,$y] is $current" }
            if (current != ROCK) continue

            var targetY: Int? = null
            log { "---  from ${y - iterateOnY.step} toward ${iterateOnY.first}" }
            for (newTargetY in y - iterateOnY.step toward iterateOnY.first) {
                val target = get(x,newTargetY)
                log { "---  check [$x,$newTargetY] = $target" }
                if (target == ROCK || target == BLOCK) break
                targetY = newTargetY
            }

            log { "---    . new target [$x,$targetY]" }
            set(x, y, EMPTY)
            set(x, targetY ?: y, ROCK)

            log { "---     targetField: \n ${map { "-- ${it.map { it }}\n" }}" }
        }
    }

    log { "Result Field: \n ${map { "-- ${it.map { it }}\n" }}" }
}

private fun Field.get(x: Int, y: Int) = get(y)[x]
private fun Field.set(x: Int, y: Int, c: Char) {
    get(y)[x] = c
}

fun log(s: ()->String) {
    if (false) println(s)
}

fun List<CharArray>.column(col: Int): CharArray = indices
    .map { get(it)[col] }
    .toCharArray()

private fun readInput(name: String): List<CharArray> = Path("./", "$name.txt")
    .readLines()
    .map { it.toCharArray() }

private infix fun Int.toward(to: Int): IntProgression {
    val step = if (this > to) -1 else 1
    return IntProgression.fromClosedRange(this, to, step)
}
