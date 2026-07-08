# Rubric

- Problem slug: `reverse-nodes-in-k-group`
- Archive path: `archives/2026-07-07-reverse-nodes-in-k-group/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly restate that groups of size < k at the tail are left untouched | Problem Summary and Edge Cases in blog both state this correctly. | met |
| Constraint analysis | Recognize k can equal n (single group) and k can be 1 (no-op) as boundary cases | Both listed correctly in blog Edge Cases and verified by tests. | met |
| Brute-force construction | Optional: could describe a buffer-and-relink approach before in-place | Blog describes array-collect-and-relink, O(n) space, correctly distinguished from final O(1)-space algorithm. | met |
| Pattern recognition | Generalize the pairwise-swap pattern (LC 24) to parameterized group size k; recognize need for a lookahead check before committing to reverse | Independently framed Key Insight as "check k nodes exist before reversing, or already-reversed nodes would be wrong." Pattern-recognition section explicitly names the group_prev/group_head/kth/group_next bookkeeping as the generalized shape. | met |
| Invariant formulation | State what `group_prev` represents at each outer-loop iteration | Correctness Argument states it precisely: "group_prev points to the node right before the next group that has not been processed yet." | met |
| Complexity analysis | State O(n) time / O(1) space unprompted | Stated correctly in blog (agent-filled section, left unmodified — no new evidence of unprompted recall this session). | not newly tested |
| Edge-case design | Cover empty list, k=1, k=n, exact multiple, remainder shorter than k | All covered (agent-filled, unmodified by user). | met |
| Debugging discipline | Track any bugs and how they were resolved | Two mechanical bugs (`true`/`True`, `kth` not advancing), both self-fixed within one guided question each; reversal loop itself was correct on first fill. Zero logical bugs in final code. | met |
| Communication | Blog accuracy on first submission | Mistakes Made section is fully accurate against actual git history — first zero-fabrication blog in the linked-list arc's Mistakes section. Blog accepted with zero revisions. | met |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Concrete trace requests: 3 (kth-advancement trace, IndentationError run-it-yourself, NameError run-it-yourself)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Strong session. The user independently generalized the swap-nodes-in-pairs pairwise-rewiring pattern to an arbitrary group size k, correctly identifying the need for a lookahead check before committing to any reversal — this was the predicted next step from the prior session's algorithm-progress notes, and it transferred cleanly. Both bugs were mechanical (a non-Python `true` literal, and a lookahead pointer that needed an explicit `.next` advance), surfaced through targeted trace questions and self-fixed by the user without direct explanations. Zero logical bugs. The blog broke a recurring pattern from several previous sessions (misattributed or fabricated entries in Mistakes Made) — this is the first blog in the arc accepted with zero revisions and zero inaccurate content in that section.
