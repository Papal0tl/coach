# Rubric

- Problem slug: `flatten-binary-tree-to-linked-list`
- Archive path: `archives/2026-07-27-flatten-binary-tree-to-linked-list/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Restates in-place pre-order-linked-list requirement in own words | Blog Problem/Key Insight sections restate it accurately | met |
| Constraint analysis | Notes n up to 2000, small enough for O(n) recursion | Not explicitly discussed | not observed |
| Brute-force construction | Collect pre-order list, then relink | Blog's Brute Force section describes this correctly and distinctly from Final Algorithm | met |
| Pattern recognition | Recognizes this as pre-order traversal + in-place relinking (11th tree session) | First attempt went directly to a correct recursive splice, zero bugs, zero hints | met, strong |
| Invariant formulation | States what's true about the already-flattened left subtree before attaching it | Blog's Correctness Argument states the recursive invariant clearly | met |
| Complexity analysis | O(n) time, O(h) recursion space (or O(1) extra for Morris-style follow-up); catches O(n^2) risk if repeated tail-walking is used naively | Asked twice to trace the O(n^2) left-skewed-chain case; declined both times by moving to the blog. Complexity section is agent-filled, not user-derived | not met — declined |
| Edge-case design | Empty tree, single node, left-only chain, right-only chain | Agent-filled checklist in blog matches test suite; not separately probed with the user | partially observed |
| Debugging discipline | Runs code rather than only mentally tracing | No bugs occurred, so not exercised this session | not applicable |
| Communication | Explains reasoning in English | All user-filled blog sections written clearly in English, unprompted | met |

## Intervention Count

- Clarifying questions: 2 (complexity trace question, asked twice, declined both times)
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Twelfth tree-traversal session overall (first requiring in-place restructuring of the tree itself rather than traversing, combining, validating, building, or BFS-extracting from it). The user went directly from an empty stub to a fully correct recursive post-order splice solution, zero bugs, all 6 reference tests passing on the first attempt — one of the cleanest first-attempt results in the arc. The one open item is complexity analysis: the implementation has a non-obvious O(n^2) worst case (repeated tail-walking on a left-skewed tree) that the user did not engage with when asked twice, choosing to move to the blog instead. The blog itself was otherwise fully self-written and accurate, including a correctly-scoped "N/A" Mistakes Made section verified against git history. Overall: strong algorithmic transfer, first clear instance of a declined *complexity* discussion (as opposed to previously-declined optional alternate-implementation follow-ups).
