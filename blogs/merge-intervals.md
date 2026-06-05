# Merge Intervals

**Source:** LeetCode 56 · Medium
**Date:** 2026-06-05
**Language:** Python

---

## Problem Summary

Given an array of intervals `[start, end]`, merge all overlapping intervals and return the minimal set of non-overlapping intervals that covers the same range. Touching intervals (e.g., `[1,4]` and `[4,5]`) count as overlapping.

---

## Initial Intuition

*(Write in your own words: what was your first instinct when you read the problem? Did you think about brute force, sorting, or something else?)*

---

## Brute Force

*(Describe a naive approach. What would you check, and why is it slow?)*

---

## Key Insight

*(What unlocks the efficient solution? Why does sorting matter, and what does it let you do in the scan?)*

---

## Final Algorithm

1. Sort `intervals` by start value.
2. Seed the result: `res = [intervals[0]]`.
3. For each subsequent interval `[s, e]`:
   - If `s <= res[-1][1]` (overlaps or touches): extend → `res[-1][1] = max(res[-1][1], e)`
   - Else: no overlap → `res.append([s, e])`
4. Return `res`.

---

## Correctness Argument

*(Why does this work? Why is it safe to only ever compare against `res[-1]` and never look further back?)*

---

## Complexity

- **Time:** O(n log n) — sorting dominates; the scan is O(n).
- **Space:** O(n) — the output holds up to n intervals.

---

## Edge Cases

- **Single interval:** loop body never runs; the seed is returned as-is. ✓
- **All overlapping:** one interval grows to span everything. ✓
- **Touching intervals** (`end == next start`): `<=` catches this. ✓
- **Fully contained** (e.g., `[1,10],[2,5]`): `max` on the end keeps the wider bound. ✓
- **Already sorted:** sort is a no-op; algorithm still correct. ✓

---

## Mistakes Made

*(What went wrong during your attempt? What did you fix and why?)*

---

## How to Recognize This Pattern Next Time

*(What signals in a problem should make you think "sort + linear scan with a running merged interval"?)*
