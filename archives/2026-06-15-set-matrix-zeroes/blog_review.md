# Blog Review — set-matrix-zeroes

## Correctness

All content is correct. The key insight, algorithm steps, complexity, and edge cases are accurate.

## Key Insight

Clearly stated: separate recording from modifying, and reuse the first row/col as marker space with two booleans to protect them. This is the right level of precision.

## Invariant

Partially named. The correctness argument says "matrix[i][0] == 0 is row i originally contained zero" — correct, but the phrasing is slightly off grammatically ("if row i" not "is row i"). More importantly, the invariant could be stated more crisply as a named invariant:

> **Invariant**: after the marking pass, `matrix[i][0] == 0` iff row `i` contained an original zero (for i ≥ 1), and `matrix[0][j] == 0` iff col `j` contained an original zero (for j ≥ 1).

The user's version implies this but doesn't state it as a clean iff.

## Complexity

Correct.

## Edge Cases

Correct and complete.

## Mistakes Made

Strong section. Five specific, accurate bugs are listed. Notable: mistake #4 (matrix[0][0] cannot independently represent both row 0 and col 0) shows clear understanding of the subtlest edge case.

## Transfer Readiness

The "How to Recognize" section is thin: "Asks for an in-place matrix modification and the naive solution needs extra row/column tracking arrays." This is true but generic. What specifically triggers the border-as-marker idea vs. just using O(m+n) sets? The sharper signal is: **the problem asks for O(1) extra space AND the matrix has a border whose structure can encode the same information**. Without naming the O(1) constraint as the trigger, the pattern doesn't transfer cleanly to other problems.

## Assessment

**Accept with one minor revision request.**

The blog is concise, correct, and specific about the bugs. The only meaningful gap is the transfer-readiness signal — sharpen the "How to Recognize" section to name the O(1) space constraint as the specific trigger for the border-as-marker trick.
