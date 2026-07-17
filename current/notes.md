# Session Notes

- Problem slug: `symmetric-tree`
- Archive path: `archives/2026-07-17-symmetric-tree/`

## Agent Preparation

- Pattern: Recursive tree comparison — instead of recursing on one tree, recurse on a *pair* of subtrees that must mirror each other. Fourth tree-recursion shape in the arc, after visit (LC 94), reduce-to-scalar (LC 104), and mutate-and-return (LC 226).
- Key insight: A tree is symmetric iff its left and right subtrees are mirror images of each other. "Mirror images" isn't "equal" — it's a *recursive* relation: two nodes mirror each other iff their values match and `t1.left` mirrors `t2.right` AND `t1.right` mirrors `t2.left` (the child comparison is crossed, not parallel). This means `isSymmetric` itself can't be directly recursive on a single node; it needs a two-argument helper `is_mirror(t1, t2)`.
- Invariant or state: `is_mirror(t1, t2)` returns `True` iff the subtrees rooted at `t1` and `t2` are mirror images of each other (same shape, values equal at mirrored positions).
- Complexity target: O(n) time (every node visited once), O(h) space for the recursive call stack (O(n) worst case on a skewed tree), or O(n) space for the iterative BFS-with-queue version (holds up to a full level of node pairs).

## Reference Solution Summary

Two equivalent solutions written:
1. `isSymmetric` (recursive): base case `root is None -> True`, then delegates to `_is_mirror(root.left, root.right)`. `_is_mirror` has 3 base cases (both None -> True; exactly one None -> False; values differ -> False) and one recursive case that crosses the children: `_is_mirror(t1.left, t2.right) and _is_mirror(t1.right, t2.left)`.
2. `isSymmetricIterative`: same crossed-pair comparison, but pairs are pushed onto a queue instead of the call stack — a queue of `(t1, t2)` node pairs, processed with the same three base cases and the same crossed enqueue order (`(t1.left, t2.right)`, `(t1.right, t2.left)`).

Both pass all 6 reference tests.

## Edge Cases

- Empty tree (`root is None`) — vacuously symmetric, `True`.
- Single node — symmetric, `True` (no children to compare).
- Symmetric values but asymmetric *shape* (e.g. `[1,2,2,None,3,None,3]`) — must return `False`; a values-only comparison without shape-awareness would get this wrong.
- One side missing a child the other side has (e.g. `[1,2,2,None,2]`) — must return `False`; this is the classic "compared None against a real node" case.
- Duplicate values across different subtrees that aren't actually mirrors — values matching isn't sufficient, structure must also match at every level.

## User-Facing Takeaways

- This is the first tree session where the recursion argument is a *pair* of nodes rather than a single node — worth watching whether the user reaches for a two-argument helper independently or first tries to force `isSymmetric(root)` itself to recurse on one child at a time.
- This problem's own follow-up (recursive AND iterative) is a natural opening to make the iterative traversal a first-class task rather than an offered-and-declined extra, given three prior tree sessions (LC 94, 104, 226) all declined the iterative alternative.

## Follow-Up Candidates

- Iterative (BFS/queue) version — built into this problem's own follow-up, not a separate stretch goal this time.
- Path Sum (LC 112) or Same Tree (LC 100) as adjacent "compare/traverse with a condition" variants if a lighter follow-up is wanted instead of the iterative version.
