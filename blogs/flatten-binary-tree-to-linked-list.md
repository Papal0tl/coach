# Flatten Binary Tree to Linked List

- Problem slug: `flatten-binary-tree-to-linked-list`
- Archive path: `archives/2026-07-25-flatten-binary-tree-to-linked-list/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Agent-filled.

Given the root of a binary tree, flatten it in place into a "linked list": reuse the same `TreeNode` objects, always set `left` to `None`, and chain nodes together via `right` in the same order as a pre-order traversal (root, then left subtree, then right subtree).

## My Initial Intuition

User-filled.

_Guiding question: before you wrote any code, what was your first idea for how to turn a tree into this right-only chain — did you think in terms of "collect nodes, then relink" or "relink as you go"?_

## Brute Force

User-filled.

_Guiding question: what would the simplest correct (not necessarily in-place) solution look like — e.g., collect a pre-order traversal into a list first, then rebuild the chain from it? How does that compare in space to what you actually wrote?_

## Key Insight

User-filled.

_Guiding question: what is the one fact that tells you where to attach a node's original right subtree once its left subtree has been flattened? (Hint: think about which node in the flattened left subtree is "last" in pre-order.)_

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

1. Recursively flatten `root.left` and `root.right` first (post-order).
2. Save `left = root.left`, `right = root.right`; set `root.left = None`, `root.right = left`.
3. Walk `cur` from `root` along `.right` until `cur.right is None` — this is the tail of the newly attached (already-flattened) left chain.
4. Attach `cur.right = right`.
5. Base case: `root is None` returns immediately.

## Correctness Argument

User-filled, with agent prompts if needed.

_Guiding question: why is it safe to always attach the original right subtree at the tail of the flattened left chain, rather than anywhere else? What invariant does the recursion give you about `root.left` and `root.right` by the time you reach step 2 (i.e., what do you already know is true about them)?_

## Complexity

Agent-filled; user should confirm they understand it.

Time: this specific implementation is **not** O(n) in the worst case. Each call re-walks the entire newly-attached left chain to find its tail via `while cur.right`. On a left-skewed tree (every node has only a left child), the walk length at depth `k` from the bottom is proportional to `k`, so the total work is `1 + 2 + ... + n = O(n^2)`. On a balanced or right-skewed tree it is closer to O(n), but the worst case is O(n^2).
Space: O(h) recursion stack, where `h` is the tree height (up to O(n) for a skewed tree).

The reference solution avoids this by using an iterative Morris-style walk that finds each node's splice point exactly once overall, giving true O(n) time and O(1) extra space.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root is None`).
- Single node (no children).
- Left-only chain (every node has only a left child) — the case that exposes the O(n^2) worst case.
- Right-only chain already (no node has a left child) — should be a no-op.
- Mixed left/right children across multiple levels.

## Mistakes I Made

User-filled.

_Guiding question: check `attempt.py`'s git history for this problem — were there any real bugs along the way, or did the first draft already pass all tests? Be precise about what actually happened rather than what could plausibly have gone wrong._

## How I Will Recognize This Pattern Next Time

User-filled.

_Guiding question: what's the general shape of problems where you need to restructure a tree in place based on traversal order, and what should make you reach for "attach at the tail of the already-processed subtree" as a technique?_
