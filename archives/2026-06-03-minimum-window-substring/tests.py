from agent_solution import min_window


def test_example1():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"

def test_example2():
    assert min_window("a", "a") == "a"

def test_example3_no_solution():
    # t has two 'a' but s has only one
    assert min_window("a", "aa") == ""

def test_t_longer_than_s():
    assert min_window("ab", "abc") == ""

def test_full_string_is_answer():
    assert min_window("ABC", "ABC") == "ABC"

def test_duplicates_in_t():
    # Need two 'a's; smallest window is "aa"
    assert min_window("aabc", "aa") == "aa"

def test_single_char_repeated():
    assert min_window("bba", "ab") == "ba"

def test_window_not_at_end():
    # Minimum window is at the start
    assert min_window("ABCXYZ", "ABC") == "ABC"

def test_overlapping_candidates():
    # Multiple valid windows; pick the shortest
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"

def test_s_equals_t():
    assert min_window("XYZ", "XYZ") == "XYZ"


if __name__ == "__main__":
    tests = [
        test_example1, test_example2, test_example3_no_solution,
        test_t_longer_than_s, test_full_string_is_answer,
        test_duplicates_in_t, test_single_char_repeated,
        test_window_not_at_end, test_overlapping_candidates,
        test_s_equals_t,
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
