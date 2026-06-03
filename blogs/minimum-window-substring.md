# Minimum Window Substring

**Source:** LeetCode 76 · Hard
**Date:** 2026-06-03
**Language:** Python

---

## Problem Summary

Given strings `s` and `t`, find the shortest contiguous substring of `s` that contains every character of `t` (including duplicates). Return `""` if none exists.

---

## Initial Intuition

TODO: What was your first instinct when you read this problem? Did you think of brute force, or did a pattern come to mind immediately?

---

## Brute Force

TODO: Describe the brute force approach in your own words. What is its time complexity and why is it too slow?

---

## Key Insight

TODO: What is the insight that makes O(m + n) possible? Why does a sliding window work here, and what tells you when to stop expanding vs. when to shrink?

---

## Final Algorithm

1. Build `need` — frequency map of all characters in `t`. Set `required = len(need)`.
2. Expand right pointer `r` across `s`. Add `s[r]` to the window frequency map. If its count reaches the required count, increment `formed`.
3. While `formed == required` (window is valid):
   - Record the window if it's the smallest seen so far.
   - Remove `s[l]` from the window. If that drops its count below required, decrement `formed`. Advance `l`.
4. After scanning all of `s`, return the best window, or `""` if none was found.

---

## Correctness Argument

TODO: Why does this algorithm never miss the optimal window? Specifically: why is it safe to shrink from the left the moment the window is valid?

---

## Complexity

- **Time:** O(m + n) — each character in `s` is added and removed at most once; building `need` takes O(n).
- **Space:** O(52) — the two frequency maps hold at most 52 distinct English letters.

---

## Edge Cases

- `t` has duplicate characters: `need` stores full counts; `formed` only increments when `window[c]` *reaches* `need[c]`, not just when it's nonzero.
- No valid window exists: `min_len` stays at infinity, return `""`.
- `len(t) > len(s)`: can never be satisfied, returns `""` naturally.

---

## Mistakes Made

TODO: What bugs or wrong turns did you hit during this session? What did each one teach you?

---

## How to Recognize This Pattern Next Time

TODO: What is the signature of a problem that calls for this technique? What keywords, constraints, or problem shapes should trigger "sliding window with a coverage counter"?
