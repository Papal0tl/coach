# Rubric

- Problem slug: `diameter-of-binary-tree`
- Archive path: `archives/2026-07-17-diameter-of-binary-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly distinguish "diameter" (edges between two nodes) from "height"/"depth" (edges to a leaf) | Went straight to a height-based recursive helper, no confusion between the two concepts in the initial approach | met |
| Constraint analysis | Recognize diameter may not pass through root | Not explicitly discussed; solution's per-node update handles it correctly by construction | not directly observed |
| Brute-force construction | Consider O(n^2) (recompute height at every node) before optimizing to single-pass | Went directly to single-pass; brute force not attempted or discussed | not observed |
| Pattern recognition | Transfer recursive bottom-up combine from maximum-depth-of-binary-tree | First draft already had the right overall recursive shape (helper computing depth, combining child results) | met |
| Invariant formulation | Separate "value returned to caller" (height) from "value tracked as running best" (diameter) | This was the core bug: conflated the two for 4 drafts (returning the diameter-like sum, not the height; and not persisting the running best via a shadowed local). Resolved only after two rounds of guided questions, landing on `self.length` for the tracked value and `1 + max(left, right)` for the returned height | needed scaffolding, resolved correctly |
| Complexity analysis | State O(n) time / O(h) space unprompted | Not asked this session | not observed |
| Edge-case design | Empty tree, single node, skewed tree, non-root diameter | Not designed by the user; covered by the pre-written reference test suite, all passed | not observed (tests were agent-authored) |
| Debugging discipline | Run code rather than predict output (established strength) | Continued strength: every fix was verified by running the code and reading the actual error/output, never by mental trace alone | met |
| Communication | Blog Mistakes Made completeness (recurring watch area) | pending — blog not yet written | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 5 (run-it prompts / trace requests: syntax error x2, missing-arg error, wrong-answer trace, scoping-rules question, assignment-site enumeration question)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Fifth tree session, first with a genuine scoping/invariant bug rather than a purely mechanical one. The recursive shape (post-order combine) transferred correctly on the first draft; the real difficulty was separating the returned height from the tracked-as-side-effect diameter, which took two guided-question rounds to resolve (first question surfaced the concept but didn't land the fix; a follow-up asking to enumerate assignment sites did). Final fix (`self.length` instance attribute) was self-chosen, not the literally hinted `nonlocal`. Blog review requested one revision (3 omitted mechanical bugs in Mistakes I Made); the user declined it, closing the session with only the conceptual bug documented — the first declined blog revision since the merge-k-sorted-lists/sort-list stretch (2026-07-10/11), after four consecutive accepted revisions (remove-nth-node-from-end-of-list, copy-list-with-random-pointer, maximum-depth-of-binary-tree) and clean sessions in between.
