# Rubric

- Problem slug: `binary-tree-level-order-traversal`
- Archive path: `archives/2026-07-18-binary-tree-level-order-traversal/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly identify this needs level-by-level grouping, not just any traversal order | Not verbally stated, but code correctly groups by level from the first draft | Met (implicit) |
| Constraint analysis | Note the [0, 2000]-node bound and empty-tree case | Not explicitly discussed; empty-tree guard was present in code from the first draft | Not observed (verbally) |
| Brute-force construction | Reach for a queue-based BFS rather than forcing a DFS/recursive shape | First draft went straight to `deque` + level-size-snapshot BFS, zero hints | Met |
| Pattern recognition | Recognize this as BFS, distinct from the five prior DFS-shaped tree sessions | Correctly reached for a queue-based approach despite five straight recursive-DFS tree sessions immediately prior | Met |
| Invariant formulation | Articulate the level-size-snapshot invariant (queue holds exactly one level at loop top) | Stated precisely when asked: "queue contains exactly the nodes of one level... size is saved before processing so only those nodes are removed" | Met (prompted) |
| Complexity analysis | State O(n) time / O(n) space unprompted | Asked, not volunteered; answer separated queue space `O(w)` from overall space `O(n)`, more precise than the reference notes | Exceeded (prompted) |
| Edge-case design | Cover empty tree, single node, skewed tree, uneven levels | All covered by the provided reference test suite; no additional user-authored edge cases | Met (via provided tests) |
| Debugging discipline | Run code rather than mentally trace when bugs appear | Ran the file, read the actual `NameError` traceback, fixed independently with no explanation needed | Met (strong) |
| Communication | English, clear reasoning in comments/blog | English throughout; invariant and complexity answers were clear and precise | Met |

## Intervention Count

- Clarifying questions: 0
- Hints: 1 (prompted to run the code rather than mentally trace, after the `deque([root])` fix)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Zero logic bugs; two mechanical bugs (`deque(root)` vs `deque([root])`, missing `from collections import deque`), both self-fixed after seeing the real traceback rather than a hint. First BFS session in the tree arc after five consecutive DFS sessions — the queue-based shape transferred cleanly with no scaffolding needed, unlike some earlier DFS-shape transfers (e.g. symmetric-tree's pair-recursion). Invariant and complexity reasoning were both precise on request, with the complexity answer exceeding the reference solution's own notes in rigor (queue-width vs. overall-space distinction). Strongest first-attempt signal for a new *traversal strategy* (not just new recursive shape) so far in the arc.
