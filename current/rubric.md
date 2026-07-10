# Rubric

- Problem slug: `sort-list`
- Archive path: `archives/2026-07-10-sort-list/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names the constraint that a linked list can't be randomly indexed, ruling out array-style sorts | Blog Key Insight states this explicitly and correctly | met |
| Constraint analysis | Recognizes O(n log n) time is required (rules out insertion/selection sort) and considers the O(1)-space follow-up | Blog Complexity section (agent-drafted) confirmed; O(1)-space follow-up not attempted this session (not offered as a distinct task) | partially met |
| Brute-force construction | Describes an O(n) space approach (dump values into an array, sort, rebuild list) as a valid but non-optimal baseline | Blog Brute Force describes a genuinely distinct array-based approach with correct O(n log n)/O(n) complexity | met |
| Pattern recognition | Identifies merge sort as the natural fit; reuses fast/slow midpoint-finding and two-list merge from prior sessions | First draft was a bubble-sort-style adjacent swap, not merge sort; pivoted independently to fast/slow split + merge (reusing merge-two-sorted-lists) after discovering the swap approach broke reachability | met (after a self-directed pivot, not on the first attempt) |
| Invariant formulation | States why the recursive base case (length 0 or 1) is already sorted, and why merging two sorted halves yields a sorted whole | Blog Correctness Argument (revised) states this precisely: base case, recursive sorted-halves guarantee, and the merge-step comparison argument including tail-attach reasoning | met |
| Complexity analysis | States O(n log n) time / O(log n) space (recursive) unprompted; aware O(1) space needs an iterative bottom-up variant | Blog Complexity (agent-drafted) confirmed; not independently derived or discussed this session | met (confirmed, not derived) |
| Edge-case design | Covers empty list, single node, two nodes, duplicate values | Blog Edge Cases (agent-drafted) confirmed; all covered by the 8-case reference test suite, which the final attempt passes in full | met |
| Debugging discipline | Traces the split step carefully (severing `slow.next`) since a missed severance causes infinite recursion or duplicated nodes | Found an independently correct alternative split (tracking `prev` inside the loop) rather than the hinted `fast = head.next` offset, and verified it by hand-tracing `[2,1]` and `[4,2,1,3]` when asked; later bugs (NameError x2, missing merge tail-attach) were resolved by actually running the code and reading output/tracebacks rather than declining to trace | met |
| Communication | Clear English reasoning; notes the reuse of fast/slow and merge sub-patterns from prior sessions | Blog Key Insight and How I Will Recognize sections both explicitly name the divide-and-conquer shape and the reuse of fast/slow + merge; Mistakes Made section, however, contains fabricated/misattributed bugs and omits the real ones (see below) | partially met |

## Intervention Count

- Clarifying questions: 3 (what does the function return; what happens to the node before `cur`; what does `fast` hold at loop-exit)
- Trace requests: 3 (swap on `[4,2,1,3]`; midpoint loop on `[2,1]`; re-trace after each fix)
- Hints: 1 (invariant-level hint on the midpoint offset, after the user asked directly for one)
- Direct explanations: 0
- Code-level nudges: 0 (no code written for the user; every fix was the user's own edit)

## Closeout Assessment

Strong overall session with a clean pivot away from an incorrect approach. The first draft (single-pass adjacent-node swap) was abandoned unprompted after the user empirically discovered it broke list reachability — a good instance of using running/tracing to self-correct strategy, not just syntax. The subsequent fast/slow-based split, recursive sort, and merge sequence composed two previously-mastered sub-patterns (fast/slow pointer from linked-list-cycle/palindrome-linked-list; two-pointer merge from merge-two-sorted-lists) correctly, and the user found a genuinely valid alternative midpoint-finding technique (tracking `prev` inside the loop) rather than the hinted starting-offset approach — a meaningful, independent variation, not a mistake. All remaining bugs after that point were mechanical (bare function call instead of `self.sortList`, `right` vs `fast`/`slow` variable confusion, a `dummy` used before definition, a missing merge tail-attach) and were each resolved by the user after being shown the actual runtime behavior (error message or wrong output), consistent with the established empirical-debugging preference from copy-list-with-random-pointer. All 8 reference tests pass on the final `attempt.py` with zero remaining logic bugs. The blog's Correctness Argument was revised to a precise, complete statement after being flagged as blank. The Mistakes Made section, however, repeats the long-standing misattribution/fabrication pattern in a new, more pronounced form: two of its four bullets describe bugs that never happened (an `AttributeError` prevented by the loop's own guard clause; a "`tmp = cur; cur = tmp`" description that doesn't match the actual swap code) while the two most basic real bugs (missing `return` statement; two separate `NameError`s) and the merge tail-attach omission are missing entirely. This revision was requested and explicitly declined by the user. Overall: excellent algorithmic transfer and self-correction; the persistent gap remains specifically in the fidelity of the Mistakes Made write-up, now trending toward fabrication rather than omission alone.
