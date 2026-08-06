# Blog Review

- Problem slug: `rotting-oranges`
- Archive path: `archives/2026-08-05-rotting-oranges/`
- Blog path: `blogs/rotting-oranges.md`

## Correctness

Correct throughout. The algorithm description (multi-source seeding, level-by-level BFS draining exactly `size = len(queue)` cells per minute, `fresh == 0` guard on the final return) matches both `current/agent_solution.py` and the final, passing `current/attempt.py`. Complexity (O(m*n) time and space) is stated correctly with accurate justification for both bounds.

## Missing Concepts

None. The Key Insight section correctly names the two load-bearing ideas — seed all rotten cells into the queue at once (multi-source), and treat one full BFS level as one minute — without conflating them. The Correctness Argument is the strongest part of the blog: it explicitly explains *why* `size = len(queue)` must be snapshotted before the inner loop starts (so cells added during this level aren't processed until the next one), and directly answers the counterfactual ("if we increased minutes for every popped cell, the time would depend on how many oranges were processed, instead of how many minutes actually passed"). This is a clean, self-generated invariant statement.

## Clarity

Concise and precise throughout — no padding, no vague phrasing. Every section says exactly what it needs to and stops.

## Transfer Readiness

High. "How I Will Recognize This Pattern Next Time" correctly generalizes past the specific problem: "If something spreads from multiple starting points at the same time and I need to find how long it takes, I should think of multi-source BFS" — this is the right level of abstraction (spread + timing + multiple sources), not a restatement of the orange-specific mechanics. Combined with the Correctness Argument, this session shows strong readiness to recognize and apply multi-source BFS on a new problem (e.g. Walls and Gates, 01 Matrix — both already noted as follow-up candidates in `current/notes.md`).

## Required Revisions

**Mistakes Made is incomplete.** The blog reports one real bug:

> I initially allowed rot to spread through empty cells (0), instead of only spreading to directly adjacent fresh oranges (1). This caused oranges that should stay fresh to become rotten.

This is accurate and matches the fix in commit `09c4f7b`. But the git history (`current/attempt.py`) shows three other real, logic-level bugs from this same session that are not mentioned:

1. **Wrong queue payload.** Commit `4507860` pushed `queue.append(rows)` — the integer row count — instead of the cell's coordinates. Fixed in `3689db3` to `queue.append((r, c))`. (You caught and named this one verbally in the session — "oh it's just pushing the number of rows, not the coordinates" — before it was fixed in code.)
2. **Off-by-one bounds check.** Commit `3689db3` introduced `0 < nr < rows and 0 < nc < cols`, which excludes row/column index 0 from ever being a valid neighbor. Fixed in `b29c89c` to `0 <= nr < rows and 0 <= nc < cols`.
3. **Missing `fresh == 0` guard on the return.** Introduced in `9dfaf9a` (`return min` unconditionally), which would return a minute count even when some fresh orange was never reached. Fixed in the same commit as the empty-cell bug, `09c4f7b`.

Please add these three to the Mistakes Made section (or explain if you remember them differently — happy to look at the diffs together). This isn't about padding the list; bug 1 in particular is worth keeping because you diagnosed it correctly before fixing it, which is a good, citable example of your own debugging process working.

## Agent Assessment

Once Mistakes Made is revised to include all four real bugs, this session is ready to close. Everything else — algorithm, invariant, correctness argument, complexity, edge cases, and pattern transfer — is accurate and clearly written on the first draft, with no revision needed.

## Review Status

Revision requested; declined by user ("just move to archive and push to github"). Mistakes Made in the published blog names only 1 of 4 real bugs (the empty-cell/fresh-value-check bug); the queue-payload bug (`4507860`->`3689db3`), the off-by-one bounds check (`3689db3`->`b29c89c`), and the missing `fresh == 0` return guard (`9dfaf9a`->`09c4f7b`) are omitted. Session otherwise complete.
