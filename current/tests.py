"""
Tests for Number of Islands.
"""

from agent_solution import Solution


def test_example_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().numIslands(grid) == 1


def test_example_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().numIslands(grid) == 3


def test_single_cell_land():
    assert Solution().numIslands([["1"]]) == 1


def test_single_cell_water():
    assert Solution().numIslands([["0"]]) == 0


def test_all_water():
    grid = [["0", "0"], ["0", "0"]]
    assert Solution().numIslands(grid) == 0


def test_all_land():
    grid = [["1", "1"], ["1", "1"]]
    assert Solution().numIslands(grid) == 1


def test_diagonal_not_connected():
    grid = [
        ["1", "0"],
        ["0", "1"],
    ]
    assert Solution().numIslands(grid) == 2


def test_non_square_grid():
    grid = [
        ["1", "1", "1"],
    ]
    assert Solution().numIslands(grid) == 1


def test_narrow_column():
    grid = [["1"], ["1"], ["0"], ["1"]]
    assert Solution().numIslands(grid) == 2


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_single_cell_land()
    test_single_cell_water()
    test_all_water()
    test_all_land()
    test_diagonal_not_connected()
    test_non_square_grid()
    test_narrow_column()
    print("All tests passed.")
