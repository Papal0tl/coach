# Rubric

- Problem slug: `merge-two-sorted-lists`
- Archive path: `archives/2026-07-05-merge-two-sorted-lists/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | States the splicing requirement (reuse existing nodes, not create new ones) | Blog problem summary and "how to recognize" section both state this correctly | met |
| Pattern recognition | Recognizes this as a two-pointer merge (like merge step of merge sort) | Key Insight names comparing current heads and advancing the smaller side; brute force (sort-and-rebuild) offered as contrast | met |
| Dummy node technique | Uses a dummy/sentinel head to simplify list-building edge cases | Named and applied unprompted once asked how to track "where to attach the first node" | met |
| Loop termination | Correctly handles one list running out before the other | Leftover-attachment block present in final code and passes tests; was briefly dropped mid-session but restored without being told it was missing | met |
| Edge-case design | Empty list(s), single-node lists, all-equal values | Blog edge-case checklist complete and accurate; matches reference tests | met |
| Complexity analysis | O(n + m) time, O(1) extra space | Stated correctly in the blog; never verbally confirmed by the user in conversation when asked directly (moved to blog instead) | met (written only) |
| Communication | Clear, concise blog | Clear and well-organized; one requested revision (Mistakes Made misattribution) declined by the user | met, with an unresolved revision |

## Intervention Count

- Clarifying questions: 3 (dummy-node placement, leftover-list trace, dummy vs. dummy.next)
- Hints: 2 (merge-as-array-analogy opening hint; naming-consistency hint)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Clean session on a new linked-list sub-pattern (two-list merge, as opposed to prior sessions' single-list reversal/cycle/intersection work). First code draft had the entire algorithmic shape correct (compare heads, splice smaller, advance, attach leftover) but was left incomplete (blank pointer initialization, mismatched variable names, no return value) — recovered fully after two rounds of targeted hints, including independently naming and applying the dummy-node technique. Final attempt passes all 9 tests with zero logical bugs; only mechanical bugs (a case typo, returning the sentinel instead of its `.next`). The complexity/recursive follow-up questions were skipped in favor of writing the blog, and — new this session — a requested blog revision (a mischaracterized "mistake," missing two real bugs) was explicitly declined rather than applied, so the archived blog does not fully match the actual session history. See `blog_review.md` for the specific gap.
