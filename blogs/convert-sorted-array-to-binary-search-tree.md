# Convert Sorted Array to Binary Search Tree

- Problem slug: `convert-sorted-array-to-binary-search-tree`
- Archive path: `archives/2026-07-19-convert-sorted-array-to-binary-search-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given an integer array `nums` sorted in ascending order, convert it to a height-balanced binary search tree (any valid one is accepted).

## My Initial Intuition

User-filled.

## Brute Force

User-filled.

## Key Insight

User-filled.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Recursive helper `build(left, right)` operating on an index range into `nums`. Base case: if `left > right`, return `None` (empty range). Otherwise compute `mid = (left + right) // 2`, create `TreeNode(nums[mid])`, and recursively set `.left = build(left, mid - 1)` and `.right = build(mid + 1, right)`. Top-level call is `build(0, len(nums) - 1)`.

## Correctness Argument

User-filled, with agent prompts if needed.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every element becomes exactly one `TreeNode`, created once.
Space: O(log n) additional space for the recursion call stack (tree height is O(log n) since the middle-index split keeps the tree balanced), not counting the O(n) output tree itself.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Single-element array (`[1]`) -> a single node with no children.
- Even-length array -> `mid` rounds down (integer division), so the left half gets one fewer element than the right; still balanced since heights differ by at most 1.
- Two-element array (`[1, 3]`) -> the mid-selection choice determines whether the smaller or larger value becomes the root; both are valid outputs.
- Larger inputs (up to 10^4 elements per constraints) -> recursion depth stays O(log n), no stack-depth concern.

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.
