# Session Notes: Lowest Common Ancestor of a Binary Tree

## Timeline

- 2026-07-30: Session started. Problem sourced from user-provided LeetCode.cn link.
- 2026-07-30: Agent reference solution written (bottom-up recursive search), 7/7 local tests pass.

## Key Insight (agent-only, do not reveal directly)

At any node, recursively search both subtrees for `p` and `q`. There are only
three cases to distinguish at each call:

1. The current node itself is `p` or `q` (or `None`) — return it immediately;
   no need to look further down that branch, since the ancestor definition
   allows a node to be its own descendant.
2. Both the left and right recursive calls return non-`None` — that means
   `p` and `q` were found in *different* subtrees of the current node, so
   this node is exactly the split point: the LCA.
3. Only one side returns non-`None` — both `p` and `q` (or just one of them,
   propagating upward) live in that subtree, so pass that result up
   unchanged.

## Invariant

`lowestCommonAncestor(node, p, q)` returns `p` or `q` directly if `node` is
one of them; otherwise it returns the LCA of `p` and `q` *if both exist in
node's subtree*, one of `p`/`q` if only one exists in `node`'s subtree (this
signals "found, not yet joined" to the caller), or `None` if neither exists
in `node`'s subtree.

## Complexity

- Time: O(n) — every node visited at most once.
- Space: O(h) recursion stack, where h is the tree height.

## Brute Force (for comparison)

Find the root-to-p and root-to-q paths (each via a separate DFS collecting
the path as a list of nodes), then walk both paths together and return the
last node where they still match. O(n) time (two path-finding DFS passes)
but conceptually two steps instead of one; roughly O(n) time / O(n) space
(storing both paths) versus the single-pass recursive approach's O(h) space.

## Edge Cases

- `p` is an ancestor of `q` (or vice versa) — the answer is `p` itself, not
  some node further up.
- `p` and `q` are in different subtrees at various depths (root-level split
  vs. a split deep in the tree).
- Tree is only 2 nodes.
- Skewed (linked-list-shaped) tree.
- `p` or `q` is the root itself.

## Target Coaching Skills (see rubric.md)

- First tree session requiring a search for *two* target nodes simultaneously
  and combining the two search results at each level — distinct from LC 101's
  pair-of-nodes *comparison* (symmetric-tree compares two nodes at the same
  recursive call; this problem searches for two independent targets and
  merges results bottom-up).
- Watch whether the "node can be its own ancestor" edge case is handled
  correctly without prompting (i.e., checking `root is p or root is q` before
  recursing further, rather than only checking at leaves).
- Watch whether the three-way case split (found both / found one / found
  none) is reached directly, or whether the first attempt tries to explicitly
  compute and compare root-to-node paths (the O(n) brute force) first.
