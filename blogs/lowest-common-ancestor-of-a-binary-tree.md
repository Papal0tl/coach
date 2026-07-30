# Lowest Common Ancestor of a Binary Tree

- Problem slug: `lowest-common-ancestor-of-a-binary-tree`
- Archive path: `archives/2026-07-30-lowest-common-ancestor-of-a-binary-tree/`

## Problem

Given a binary tree and two nodes `p` and `q` known to exist in it, find their
lowest common ancestor: the deepest node that has both `p` and `q` as
descendants, where a node counts as its own descendant.

## My Initial Intuition

Search the tree for p and q, and compare where they were found. Not sure at first how to use recursion to find the lowest common ancestor.

## Brute Force

Finding the path from the root to p and the path from the root to q, then comparing the two paths to find their last common node. The recursive approach was simpler because did not need to store the paths.

## Key Insight

If both left and right return a node, p and q were found on different sides, so the current root is their LCA.

If only left returns a node, the result is somewhere on the left, so return left. The same applies to the right.

If neither side returns anything, return None because neither p nor q was found there.

## Final Algorithm

The submitted solution recurses on `root`: if `root` is `None`, `p`, or `q`,
it returns `root` directly (checking for `p`/`q` before recursing further,
since a node is allowed to be its own ancestor). Otherwise it recurses into
`root.left` and `root.right`. If both recursive calls return a non-`None`
result, `p` and `q` were found in different subtrees, so `root` itself is the
LCA. If only one side returns non-`None`, that result (either the LCA already
found deeper down, or one of `p`/`q` still propagating upward to be matched
with the other) is passed up unchanged. If neither side finds anything, the
function returns `None`.

## Correctness Argument

This checks both subtrees before deciding what to return. If p and q are found on different sides, the current node is their first common ancestor from the bottom up. If the LCA is already deeper in one subtree, that result is returned upward, so a higher node will not replace it.

## Complexity

- Time: O(n) — every node is visited at most once.
- Space: O(h) for the recursion stack, where h is the tree height (O(log n)
  for a balanced tree, O(n) for a fully skewed tree).

## Edge Cases

- `p` is an ancestor of `q` (or vice versa) — answer is `p` itself, not a
  node further up.
- `p` and `q` split at the root vs. split deep in the tree.
- Tree with only 2 nodes.
- Skewed (linked-list-shaped) tree.
- `p` or `q` is the root.

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

Need to find a relationship between two nodes in a tree, should think about a bottom-up recursion. If each subtree can return useful information to its parent, combine the left and right results at the current node.
