# Blog Review — First Missing Positive

**Date**: 2026-06-11  
**Status**: Accepted

## Correctness

- Problem summary: correct.
- Key insight (bound [1, n+1], index-as-hashmap): correct and clearly stated.
- Final algorithm: correct.
- Correctness argument: the termination argument ("every successful swap places at least one value at its home") is accurate. The scan logic is correctly explained.
- Complexity: correct.
- Edge cases: correct.

## Issues Requiring Revision

### 1. Brute Force — sort approach is incomplete

The sort approach is listed but never says which constraint it violates. Sorting is O(n log n) time — that violates the **time** constraint, not the space constraint. Add one line explaining this.

### 2. Mistakes Made — second bullet reads as present confusion

> "Not sure why only care about values from 1 to n"

This reads as a current uncertainty, not a past mistake. Either:
- Rephrase as a past confusion that you now understand: "Initially unclear why values > n can be ignored — realized they can never be the smallest missing positive in [1, n+1]."
- Or remove it if it was never actually a mistake during the session.

### 3. How to Recognize — too vague, grammar error

> "missing or duplicate numbers, and the numbers are belong to a small fixed range like 1 to n"

Two issues:
- Grammar: "are belong to" → "belong to"
- Vagueness: doesn't name the pattern. What is this technique called? When exactly should you reach for it?

## What Is Good

- Initial intuition section is honest and precise about why a set fails.
- Key insight correctly names the bound and the mapping rule.
- Correctness argument states the invariant in usable form.
- Duplicate guard is identified as the key mistake — accurate.

## Transfer Readiness

Ready. User independently named the pattern (index-as-hash-map) and identified the trigger (values belong to a fixed range [1, n]). Minor phrasing issues remain in the blog but understanding is demonstrated through both the code and the written sections.
