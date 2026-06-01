from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)          # required frequency for each char in t
    required = len(need)       # number of distinct chars that must be satisfied

    have: dict[str, int] = {}  # frequency of chars in the current window
    formed = 0                 # distinct chars in window that meet their required count

    left = 0
    best_len = float("inf")
    best_left = 0

    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        # Shrink from the left while the window is valid
        while formed == required:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_left = left

            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_left : best_left + best_len]
