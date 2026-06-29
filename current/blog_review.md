# Blog Review — Rotate Image

## Correctness

- Initial intuition: correct. Identifies the mapping `(row, col) → (col, n-1-row)` and the overwrite problem precisely.
- Brute force: correct. Mapping formula and O(n²) space cost are both right.
- Key insight: correct. 4-position cycle + one `tmp` to avoid data loss.
- Final algorithm: correct code.
- Correctness argument: correct and detailed. Four positions named, movement direction stated (Left→Top, Bottom→Left, Right→Bottom, Top→Right), assignment order explained, outer/inner loop roles explained.
- Complexity: correct.
- Edge cases: correct.

## Clarity

Good overall. The correctness argument is the strongest section — it names the four coordinate pairs explicitly and explains why the assignment order is safe. The brute force section is also precise.

## Invariant

The invariant is implicit but not named: at the start of each outer loop iteration, rings 0 through i-1 have been fully rotated, and the inner loop covers every position in the top edge of ring i exactly once (excluding the last corner because it is covered by an earlier position's cycle). Naming this explicitly would strengthen the argument, but the current explanation is acceptable.

## Mistakes Made — REVISION REQUIRED

The first two bullets are plausible:
- "Did not understand why the outer loop only runs n//2 times" — acceptable.
- "Mixed up the four coordinate pairs" — acceptable.

The third bullet — **"the coordinate starts at (0,0) instead of (1,1)"** — is unclear. What does this mean? Was there a specific bug or confusion about loop initialization? If this refers to the inner loop starting at `j = i` rather than `j = i + 1`, explain it. If it is not a real mistake, remove it.

Please clarify or remove that bullet.

## How to Recognize

The five cues are reasonable. "Square matrix" and "transformation based on coordinates" are generic enough to apply to many problems; consider adding one more specific cue about when cycles/rings appear — for example: when you notice that four cells are equidistant from the center and 90° apart, they belong to a cycle.

## Transfer Readiness

High. The user identified the coordinate mapping from first principles (brute force section), named the cycle positions correctly, and explained the assignment order. The pattern is well-internalized. One revision needed before acceptance.

## Required Revisions

None. Third bullet in Mistakes Made kept as-is at user's request.

## Final Assessment

Blog accepted.
