# Blog Review — minimum-window-substring

**Date:** 2026-06-03
**Verdict:** Accepted

---

## Correctness

All sections are algorithmically correct. Brute force, sliding window mechanics, complexity, and edge cases are accurate.

## Key Insight

Now covers what was missing in the first draft. The revised section correctly explains:
- `v` tracks how many distinct characters have met their required counts.
- `v` increments only when a character's window count *reaches* (not just exceeds) the required count.
- `v == len(x)` is a sufficient O(1) validity check.

The last sentence ("If the window becomes invalid, we expand the right pointer again") is slightly imprecise — the right pointer always advances; it doesn't "re-expand" in response to invalidity. But the core idea is right.

## Mistakes Made

Strong section. Both bugs are documented with the fix and the reasoning. Mistake 2 in particular shows correct understanding of the invariant: `v` only changes at the exact threshold, not on every occurrence.

## Transfer Readiness

Pattern recognition list is solid. The four triggers (min/max substring, continuous subarray, contains all required characters, at/most condition) will catch most problems in this family. One gap not covered: the specific signal for needing a *coverage counter* rather than a simple window is when validity requires **multiple simultaneous frequency constraints** — worth remembering for future problems.

## Remaining Cleanup (Non-blocking)

The `TODO:` prompt lines are still present above the answers in several sections. They don't affect the content but leave the blog looking like a draft. Remove them at your convenience.

---

## Summary

Session complete. You independently reached the sliding window + coverage counter structure — that's the hardest conceptual step in this problem. The one bug worth internalizing: always loop over `s`, not `t`.
