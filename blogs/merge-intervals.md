# Merge Intervals

**Source:** LeetCode 56 · Medium
**Date:** 2026-06-05
**Language:** Python

---

## Problem Summary

Given an array of intervals `[start, end]`, merge all overlapping intervals and return the minimal set of non-overlapping intervals that covers the same range. Touching intervals (e.g., `[1,4]` and `[4,5]`) count as overlapping.

---

## Initial Intuition

My first idea is to keep track of the last interval that had already been processed and compare each new interval against it.

For each interval, I extracted its start and end values and compared them with the start and end of the last interval. If the current interval started before the previous merged interval ended, I considered them overlapping and merged them. Otherwise, I added the interval as a new entry in the result.

---

## Brute Force

Compare every interval with every other interval and repeatedly merge any pair that overlaps. This is slow because each interval may need to be compared with many others, leading to about O(n²) comparisons. It is also harder to manage because merging one pair may affect later comparisons.

---

## Key Insight

Key insight is to sort the intervals by their start value first. After sorting, any interval that can overlap with the current merged interval must appear immediately after it during the scan. Then only need to compare the current interval with the last merged interval in `res[-1]`, instead of checking all previous intervals.

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

After sorting, intervals are processed from left to right by start value. `res[-1]` always stores the most recent merged interval. If the current interval starts before or at `res[-1]`’s end, then they overlap, so need to extend the end. If the current interval starts after `res[-1]`’s end, then it cannot overlap with `res[-1]` or any earlier interval. So, append it as a new interval.


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

Use `intervals[i-1]` to get the previous interval’s start and end and get the value from intervals last and previous value. It should compare intervals current value with the intervals newest value.

the type of res should be [intervals[]], not res = [] and intervals[]. eg: intervals = [[1,3],[2,6],[8,10]]. Then intervals[0] is [1,3]. This is one interval. However, the final answer should be: [[1,6],[8,10]]. which is: a list of intervals not a single interval. If res = intervals[0], then: res = [1,3]. Now: res[-1], returns: 3 instead of: [1,3]. The later code will not work.

---

## How to Recognize This Pattern Next Time

Merge Intervals
Insert Interval
Meeting Rooms
Employee Free Time
Non-overlapping Intervals