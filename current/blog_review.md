# Blog Review — minimum-window-substring

**Date:** 2026-06-03
**Verdict:** Revision requested (one section)

---

## Correctness

Algorithm, complexity, and edge cases are all correct. The brute force section correctly identifies O(m²) substrings. The mistakes section accurately captures both bugs encountered in the session.

---

## Clarity

Most sections are clear and appropriately concise. One issue: several sections still contain the `TODO:` prompt text above the actual answer. Remove those lines — they leave the blog looking unfinished.

---

## Key Insight — Needs Revision

The current entry:

> sliding window [l, r]. Expand r when the window is not valid, shrink l when the window is already valid. moving r makes the window bigger, moving l makes the window smaller.

This describes **when** to move each pointer, but it skips the most important question: **how do you know in O(1) whether the window is valid?**

Checking all character counts on every step would cost O(52) per move and is not the insight. The key is the `v` counter (called `formed` in the reference): a single integer that tells you instantly whether all required characters are satisfied. It increments only when a character's window count *reaches* its required count, and decrements only when it *drops below* it.

Please revise the Key Insight section to explain the coverage counter — what it tracks, when it changes, and why it makes validity checking O(1).

---

## Correctness Argument

Acceptable. Mentions that every right endpoint is scanned and that any smaller window must come from moving `l` right. Could be sharpened: for each fixed `r`, the while-loop finds the *leftmost valid `l`*, which is the minimum-length window ending at `r`. The global minimum is the best across all `r`. But the current version conveys the essential idea.

---

## Mistakes Made

Strong section. Both bugs are described with the correct fix and a clear explanation of why. Notably, mistake 2 (the `v` condition) shows understanding of the invariant even if the code happened to get it right — good to document the conceptual trap.

---

## Transfer Readiness

Pattern recognition list is good: minimum/maximum substring, continuous subarray, contains all required characters, at least/at most condition. To sharpen it: the specific trigger for a *coverage counter* (rather than just any sliding window) is when the validity condition involves **multiple distinct requirements that must all be simultaneously satisfied** with frequency constraints. Add one bullet on that.

---

## Required Revisions

1. **Key Insight**: explain the `v`/`formed` coverage counter — what it is, when it changes, why it's O(1). (Required before session closes.)
2. **TODO lines**: remove all `TODO:` prompt text from the final blog. (Minor cleanup.)
3. **Transfer section** (optional): add a bullet about the multi-requirement / frequency-constraint trigger.
