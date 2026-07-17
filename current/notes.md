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

## Coaching Log

- First draft: `if root.left == root.right: return True else: return False`, followed by two unreachable recursive calls after the `return`. Confirms the predicted risk from "User-Facing Takeaways" — the attempt tried to make `isSymmetric(root)` recurse on a single node's two children directly, rather than reaching for a two-argument pair-comparison helper. Also has an object-identity trap (`root.left == root.right` compares `TreeNode` objects, which are never equal unless both `None`, since `TreeNode` has no `__eq__`) and dead code after the early `return`. Did not run against the reference tests before asking for a check. Intervention: asked to run the attempt against `tests.py`-style examples and predict/observe behavior, rather than being told the bugs directly.
- Second draft: rewrote the base cases to the correct three-way mirror-check shape (`both None -> True`, `one None -> False`, `values differ -> False`) — the invariant logic itself is now right, and matches the reference `_is_mirror` base cases almost exactly. But the method signature is still `isSymmetric(self, root)` (single argument), while the body references `left`/`right`, which are never defined anywhere — this is an undefined-name `NameError` waiting to happen the moment it runs. Also still recurses as `self.isSymmetric(root.left)` / `self.isSymmetric(root.right)` (single-node calls, no captured return value, no combining `and`), not a two-argument pair recursion. Ran (`NameError: name 'left' is not defined`), confirming the prediction. Asked verbally what `left`/`right` should be; answered correctly (`root.left`, `root.right`), and separately reasoned through why a single-argument `isSymmetric(root)` can't check a deeper pair like the two `3` nodes.
- Third draft: added the crossed-pair recursive calls `t1 = compare(left.left, right.right)`, `t2 = compare(left.right, right.left)`, `return t1 and t2` — this is exactly the correct crossed-mirror recursion shape (matches the reference `_is_mirror`'s recursive case precisely), a strong sign the pair-recursion insight has landed conceptually. But three issues remain: (1) `left`/`right` are still never assigned from `root` — the `NameError` from the previous draft is still live and unaddressed; (2) `compare` is called but never defined anywhere — it reads like the user wants a two-argument helper distinct from `isSymmetric`, but hasn't written it; (3) the final `return compare(root.left, root.right)` line is indented at the class-body level (4 spaces, same as `def isSymmetric`), not inside any function — `SyntaxError: 'return' outside function`. Ran and confirmed the `SyntaxError` at line 31. Also, lines 25-26 (`self.isSymmetric(root.left)` / `self.isSymmetric(root.right)`, unused return values) are now dead/leftover code from the first draft's shape. Intervention: asked a structural question about the relationship between `isSymmetric` and the not-yet-defined `compare`, and about where the entry-point call belongs, rather than directly naming the fix.
