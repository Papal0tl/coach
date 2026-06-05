from agent_solution import merge


def test_example1_basic_merge():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_example2_touching():
    # Touching intervals (end == start) must merge
    assert merge([[1,4],[4,5]]) == [[1,5]]

def test_example3_unsorted():
    # Input not sorted by start
    assert merge([[4,7],[1,4]]) == [[1,7]]

def test_fully_contained():
    # [2,5] is completely inside [1,10] — must not shrink the result
    assert merge([[1,10],[2,5]]) == [[1,10]]

def test_single_interval():
    assert merge([[3,7]]) == [[3,7]]

def test_all_overlap_into_one():
    assert merge([[1,4],[2,5],[3,6]]) == [[1,6]]

def test_no_overlap():
    assert merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]

def test_adjacent_not_touching():
    # [1,2] and [3,4]: gap between 2 and 3, should NOT merge
    assert merge([[1,2],[3,4]]) == [[1,2],[3,4]]

def test_reverse_sorted():
    assert merge([[5,6],[1,3],[2,4]]) == [[1,4],[5,6]]

def test_single_point_intervals():
    # [2,2] and [2,2] are the same point — touching, must merge
    assert merge([[2,2],[2,2]]) == [[2,2]]

def test_large_span_contains_many():
    assert merge([[1,100],[2,3],[4,5],[50,60]]) == [[1,100]]


if __name__ == "__main__":
    tests = [
        test_example1_basic_merge, test_example2_touching, test_example3_unsorted,
        test_fully_contained, test_single_interval, test_all_overlap_into_one,
        test_no_overlap, test_adjacent_not_touching, test_reverse_sorted,
        test_single_point_intervals, test_large_span_contains_many,
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
