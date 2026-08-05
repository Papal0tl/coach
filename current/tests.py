"""
Tests for Rotting Oranges.
"""

from agent_solution import Solution


def test_example_1():
    solution = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert solution.orangesRotting(grid) == 4


def test_example_2_unreachable():
    solution = Solution()
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert solution.orangesRotting(grid) == -1


def test_example_3_no_fresh():
    solution = Solution()
    grid = [[0, 2]]
    assert solution.orangesRotting(grid) == 0


def test_no_oranges_at_all():
    solution = Solution()
    grid = [[0, 0], [0, 0]]
    assert solution.orangesRotting(grid) == 0


def test_single_fresh_no_rotten():
    solution = Solution()
    grid = [[1]]
    assert solution.orangesRotting(grid) == -1


def test_single_rotten():
    solution = Solution()
    grid = [[2]]
    assert solution.orangesRotting(grid) == 0


def test_all_rotten_already():
    solution = Solution()
    grid = [[2, 2], [2, 2]]
    assert solution.orangesRotting(grid) == 0


def test_multi_source_faster_than_single_source():
    solution = Solution()
    # Two rotten sources on opposite ends spread faster than one would.
    grid = [[2, 1, 1, 1, 2]]
    assert solution.orangesRotting(grid) == 2


if __name__ == "__main__":
    test_example_1()
    test_example_2_unreachable()
    test_example_3_no_fresh()
    test_no_oranges_at_all()
    test_single_fresh_no_rotten()
    test_single_rotten()
    test_all_rotten_already()
    test_multi_source_faster_than_single_source()
    print("All tests passed.")
