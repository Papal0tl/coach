# Rubric

- Problem slug: `maximum-depth-of-binary-tree`
- Archive path: `archives/2026-07-15-maximum-depth-of-binary-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly restate "max depth = longest root-to-leaf node count" | Not explicitly stated in chat; implicit in correct code. | not observed |
| Constraint analysis | Handle empty tree (root = None) returning 0 | Fixed bare `return` to `return 0` after one guided question. | succeeded with light prompting |
| Brute-force construction | N/A (recursive definition is already near-optimal) | N/A | n/a |
| Pattern recognition | Recognize as recursive tree DFS, transferable from inorder traversal | First draft had correct base-case/recurse/combine shape with zero hints. | independent |
| Invariant formulation | State the recursive relation: depth(node) = 1 + max(depth(left), depth(right)) | Declined when asked directly; moved to blog instead. | not observed (declined) |
| Complexity analysis | O(n) time, O(h) recursion stack space | Not asked/answered this session. | not observed |
| Edge-case design | Empty tree, single node, skewed tree | All covered by reference test suite; all pass against final attempt. | met (via tests, not authored by user) |
| Debugging discipline | Run code rather than only mentally trace, per established preference | Regression: predicted "return 1" without running first; self-corrected once told to run the exact command. | mixed — declined then corrected |
| Communication | English-only reasoning | All messages in English. | met |

## Intervention Count

- Clarifying questions: 2 (invariant + follow-up question, asked together)
- Hints: 3 (run single-node case; compare bare `return` vs `return 0`; re-run after `self.` fix)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Correct recursive solution reached with zero logic bugs and zero hints on overall shape — strong pattern transfer from the immediately prior tree session. Both bugs found were mechanical (missing `self.`, bare `return`) and resolved in one guided round each. The main new signal is a debugging-discipline regression: for the first time, a predicted-but-unverified answer ("return 1") was given before actually running the code, diverging from the established pattern of converging fast via real execution. Also the first session where the invariant-articulation question itself was skipped rather than answered, and the second consecutive session declining an iterative-traversal follow-up (BFS level-count this time, explicit-stack DFS previously).
