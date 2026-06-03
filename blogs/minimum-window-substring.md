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

Try to find a substring of s that contains all characters in t.

---

## Brute Force

TODO: Describe the brute force approach in your own words. What is its time complexity and why is it too slow?

Brute force is try to check every substring:

```
for i in range(len(s)):
    for j in range(i, len(s)):
        check s[i:j+1]
```

There are about O(m^2) substrings.

For each substring, checking whether it contains all characters of t also costs time.

So for m, n = 10^5, this is far too slow.

---

## Key Insight

TODO: What is the insight that makes O(m + n) possible? Why does a sliding window work here, and what tells you when to stop expanding vs. when to shrink?

sliding window [l, r]. Expand r when the window is not valid, sheink l when the window is already valid.
moving r makes the window bigger, moving l makes the window smaller.
use v == len(x) to check whether is valid. v tracks how many distinct characters hace already met their required counts. v increases when a character's count becomes exactly equal to its required count. checking v == len(x) enough is because Once the window becomes valid, we try to shrink it from the left to find the smallest valid window. If the window becomes invalid, we expand the right pointer again.   

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

Any smaller valid window with the same r must come from moving l to the right. r scans all positions in s, every possible ending position is considered.

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

1. 
```
for r in range(len(t)):
```

It should be:

```
for r in range(len(s)):
```

because the window moves across s, not t.

2. updating v every time a needed character appears.

```
if c in x:
    v += 1
```

v should only increase when:

```
window[c] == x[c]
```

because that means this character’s required count is fully satisfied.

---

## How to Recognize This Pattern Next Time

TODO: What is the signature of a problem that calls for this technique? What keywords, constraints, or problem shapes should trigger "sliding window with a coverage counter"?

minimum / maximum substring
continuous subarray / substring
contains all required characters
at least / at most some condition
