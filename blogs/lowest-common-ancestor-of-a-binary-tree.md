# Lowest Common Ancestor of a Binary Tree

- Problem slug: `lowest-common-ancestor-of-a-binary-tree`
- Archive path: `archives/2026-07-30-lowest-common-ancestor-of-a-binary-tree/`

## Problem

Agent-filled.

Given a binary tree and two nodes `p` and `q` known to exist in it, find their
lowest common ancestor: the deepest node that has both `p` and `q` as
descendants, where a node counts as its own descendant.

## My Initial Intuition

User-filled.

What was your first idea for how to find the LCA, before writing any code?

## Brute Force

User-filled.

An alternative approach: find the root-to-`p` path and the root-to-`q` path
separately (each as a list of nodes from a DFS), then walk both paths
together and take the last node where they still match. Did you consider
this, or something else, before landing on the recursive approach you wrote?

## Key Insight

User-filled.

You correctly identified that a recursive call's result tells you where `p`
and `q` were found: both subtrees returning something means `p` and `q` split
at this node; only one subtree returning something means both targets (or
one, still being searched for) are on that side. State this in your own
words — what does each of the three return-value cases (both found, one
found, neither found) actually represent?

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

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

User-filled, with agent prompts if needed.

Why does this always find the *lowest* (deepest) common ancestor, rather than
some higher ancestor that also contains both `p` and `q`?

## Complexity

Agent-filled; user should confirm they understand it.

- Time: O(n) — every node is visited at most once.
- Space: O(h) for the recursion stack, where h is the tree height (O(log n)
  for a balanced tree, O(n) for a fully skewed tree).

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- `p` is an ancestor of `q` (or vice versa) — answer is `p` itself, not a
  node further up.
- `p` and `q` split at the root vs. split deep in the tree.
- Tree with only 2 nodes.
- Skewed (linked-list-shaped) tree.
- `p` or `q` is the root.

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.

What signals in a future problem would tell you "this needs a bottom-up
search that returns a richer signal than just found/not-found," the way this
problem did?
