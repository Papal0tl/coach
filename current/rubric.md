# Rubric

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-22-validate-binary-search-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Recognize BST validity is a global, not local, property | First attempt was a parent-only check; failed on `[5,4,6,None,None,3,7]`. User traced it, self-diagnosed the exact violation (3 < 5, an ancestor not the parent), and the revised blog states the global-vs-local distinction explicitly and generalizes it in "How I Will Recognize This Pattern Next Time." | met |
| Constraint analysis | Handle value range (32-bit) without a colliding integer sentinel | Not independently raised by the user; the `float("-inf")` sentinel in the chosen inorder approach handles this correctly by construction, and the blog's edge-case checklist (agent-filled) covers the 32-bit boundary. Not new evidence of the user reasoning about integer sentinels specifically. | partial |
| Brute-force construction | Consider naive parent-only comparison and see why it fails | This was the actual first attempt in code (not just discussed) — direct, strong evidence. | met |
| Pattern recognition | Recursive bounds propagation (or inorder traversal) | Pivoted to inorder traversal unprompted immediately after the first attempt failed; correctly recalled that a BST's inorder sequence is sorted. | met |
| Invariant formulation | State the (low, high) bound invariant per node | Did not use the bounds-propagation form; instead formulated and correctly used the equivalent inorder invariant (`self.prev` = last visited value; every subsequent value must be strictly greater). Stated precisely in the blog's correctness argument. | met (alternate invariant) |
| Complexity analysis | O(n) time, O(h) space | Blog's Complexity section is agent-prefilled and was accepted without challenge; not independently derived or verbally restated this session. | partial |
| Edge-case design | Single node, skewed tree, duplicate values, boundary values | Blog's Edge Cases section is agent-prefilled and accepted; not independently extended with cases the user found themselves. | partial |
| Debugging discipline | | Two bugs total (wrong-subtree recursion in `inorder`; the parent-only design flaw before that). Both self-diagnosed correctly from trace requests with zero direct explanations from the agent. | strong |
| Communication | | One blog revision requested (initial draft omitted the parent-only-check narrative and the global-vs-local lesson); fully and accurately applied on the first pass. | met |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0
- Trace requests: 2 (parent-only-check failure trace; inorder wrong-subtree trace)

## Closeout Assessment

Clean session with zero direct explanations and zero code-level nudges — both
bugs (naive parent-only check, then wrong-subtree recursion in the inorder
rewrite) were resolved purely through concrete-trace requests that the user
answered correctly. The standout moment is conceptual: the first attempt's
failure produced explicit, unprompted recognition that BST validity is a
global rather than local property, and this made it into the blog's pattern-
recognition section in generalized form (check local-vs-global before
picking a per-parent comparison). Complexity and edge-case analysis were
accepted from agent-prefilled sections rather than independently re-derived
this time — worth prompting for direct engagement with those sections in a
future session where the pattern is otherwise very strong. Ready to close.
