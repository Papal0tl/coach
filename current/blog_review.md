# Blog Review

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-20-validate-binary-search-tree/`
- Blog path: `blogs/validate-binary-search-tree.md`

## Correctness

Algorithm description is correct. Inorder traversal with a running `self.prev`
bound, strictly-increasing check, and the `node.right` recursion (post-fix)
all match the working `current/attempt.py`, which passes 10/10 local tests.
Complexity (O(n) time, O(h) space) and the edge-case checklist are accurate.

## Missing Concepts

The blog jumps straight to inorder traversal in "My Initial Intuition" and
never mentions the naive parent-only comparison that was actually the first
thing attempted in this session (`root.left.val >= root.val` /
`root.right.val <= root.val`, with no recursion). That attempt failed on
`[5,4,6,None,None,3,7]` — a node can satisfy its immediate parent while still
violating an ancestor further up. That failure is the core reason BST
validity is a *global* property, not a local one, and it's the most
transferable lesson from this session (it generalizes to any problem where a
"correct-looking" local check misses a non-adjacent constraint). The
"Mistakes I Made" section only covers the second bug (wrong-subtree
recursion) and omits this first one entirely.

## Clarity

Well-written and precise where it exists — the key insight and correctness
argument are both clear and accurate for the inorder approach.

## Transfer Readiness

Not yet demonstrated for the global-vs-local distinction, since the blog
doesn't mention it. Transfer readiness for the inorder-traversal pattern
itself looks solid.

## Required Revisions

- Add the naive parent-only check as the actual first attempt in either
  "My Initial Intuition" or "Brute Force" (currently "Brute Force" describes
  a different, never-attempted O(n^2) idea — that can stay, but the
  parent-only attempt should be recorded somewhere since it happened and is
  the more instructive failure).
- Add it to "Mistakes I Made": the parent-only check passed on
  `[5,4,6,None,None,3,7]` even though 3 violates ancestor 5, because it only
  compares each node to its immediate parent.
- Extend "How I Will Recognize This Pattern Next Time" with the general
  lesson: for tree validity problems, check whether a per-parent comparison
  is enough, or whether the property depends on ancestors further up — if
  the latter, propagate state (bounds, or an inorder "previous value") down
  the recursion instead of comparing only to the immediate parent.

## Agent Assessment

Strong grasp of the implemented algorithm (inorder + strictly-increasing
invariant) with zero direct explanations needed to reach a passing solution
— both bugs were self-diagnosed from trace requests. The gap is narrative,
not technical: the blog currently tells the story as if inorder traversal
was the first idea, which erases the most valuable insight of the session
(the global-vs-local trap). Requesting revision before closeout.

## Review Status

`revision requested`
