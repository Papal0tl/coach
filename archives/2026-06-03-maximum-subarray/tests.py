from agent_solution import max_subarray


def test_example1():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_example2_single_element():
    assert max_subarray([1]) == 1

def test_example3_all_positive():
    assert max_subarray([5, 4, -1, 7, 8]) == 23

def test_all_negative():
    # Must return the least-negative element, not 0
    assert max_subarray([-3, -1, -2]) == -1

def test_single_negative():
    assert max_subarray([-7]) == -7

def test_negative_prefix_ignored():
    # Negative prefix should be dropped
    assert max_subarray([-5, 3, 4]) == 7

def test_negative_suffix_ignored():
    # Negative suffix should not drag the answer down
    assert max_subarray([3, 4, -5]) == 7

def test_answer_in_middle():
    assert max_subarray([-1, 4, 3, -1, -10]) == 7

def test_large_uniform():
    assert max_subarray([10000] * 100000) == 10000 * 100000

def test_alternating():
    # Optimal: keep all since partial sums stay positive
    assert max_subarray([5, -3, 5]) == 7


if __name__ == "__main__":
    tests = [
        test_example1, test_example2_single_element, test_example3_all_positive,
        test_all_negative, test_single_negative, test_negative_prefix_ignored,
        test_negative_suffix_ignored, test_answer_in_middle,
        test_large_uniform, test_alternating,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} passed")
