# Rubric

- Problem slug: `binary-tree-maximum-path-sum`
- Archive path: `archives/2026-07-31-binary-tree-maximum-path-sum/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Distinguish "path" (any node-to-node sequence, may bend once) from a root-to-leaf or single-direction path | Not explicitly discussed this session | not observed |
| Constraint analysis | Recognize node values can be negative, so a branch must sometimes be excluded rather than always attached | First draft already clamped each child to `max(child, 0)` with zero prompting | met |
| Brute-force construction | Consider recomputing a path sum rooted at every node (O(n^2)) before optimizing to single-pass | Went directly to single-pass; brute force not attempted or discussed | not observed |
| Pattern recognition | Transfer the recursive-combine-with-tracked-side-state shape from diameter-of-binary-tree | First draft already had the right recursive skeleton (post-order dfs, a tracked side-value plus a per-call return) | met |
| Invariant formulation | Separate "value returned to caller" (best single-branch extension) from "value tracked as running best" (allowed to bend) | This was the actual bug, same family as diameter-of-binary-tree's conflation. Took 3 edits: (1) missing `dfs(root)` call, self-diagnosed unprompted after seeing `-inf`; (2) split return value from tracked best, still missing `root.val` in the tracked-best update; (3) added `root.val`, self-corrected after tracing the `[1]` case on request. Resolved with less scaffolding than the diameter session (no scoping/`nonlocal` confusion this time) | needed one trace prompt, resolved correctly |
| Complexity analysis | State O(n) time / O(h) space unprompted | Declined when asked directly; moved to blog instead | declined |
| Edge-case design | Single node, all-negative tree, negative branch clamped to 0, best path not through root | Not designed by the user; covered by the pre-written reference test suite, all 8 passed | not observed (tests were agent-authored) |
| Debugging discipline | Run code rather than predict output (established strength) | Continued strength: the missing-call bug was found by seeing the actual `-inf` output, not by mental trace | met |
| Communication | Blog Mistakes Made completeness (recurring watch area) | pending — blog not yet written | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 3 (run-it prompt for the missing call; trace request for the `[1]` case; approach-comparison prompt was not needed)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

pending
