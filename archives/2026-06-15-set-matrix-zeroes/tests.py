import copy
from agent_solution import Solution, SolutionO1


def run(sol_cls, matrix):
    m = copy.deepcopy(matrix)
    sol_cls().setZeroes(m)
    return m


def test_example1():
    inp = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    exp = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_example2():
    inp = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    exp = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_single_zero():
    assert run(Solution, [[0]]) == [[0]]
    assert run(SolutionO1, [[0]]) == [[0]]


def test_no_zeros():
    inp = [[1, 2], [3, 4]]
    assert run(Solution, inp) == [[1, 2], [3, 4]]
    assert run(SolutionO1, inp) == [[1, 2], [3, 4]]


def test_first_row_zero():
    inp = [[0, 1], [1, 1]]
    exp = [[0, 0], [0, 1]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_first_col_zero():
    inp = [[1, 1], [0, 1]]
    exp = [[0, 1], [0, 0]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_all_zeros():
    inp = [[0, 0], [0, 0]]
    exp = [[0, 0], [0, 0]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_single_row():
    inp = [[1, 0, 3]]
    exp = [[0, 0, 0]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


def test_single_col():
    inp = [[1], [0], [3]]
    exp = [[0], [0], [0]]
    assert run(Solution, inp) == exp
    assert run(SolutionO1, inp) == exp


if __name__ == "__main__":
    tests = [
        test_example1, test_example2, test_single_zero, test_no_zeros,
        test_first_row_zero, test_first_col_zero, test_all_zeros,
        test_single_row, test_single_col,
    ]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print("All tests passed.")
