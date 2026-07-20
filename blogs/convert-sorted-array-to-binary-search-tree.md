# Convert Sorted Array to Binary Search Tree

- Problem slug: `convert-sorted-array-to-binary-search-tree`
- Archive path: `archives/2026-07-19-convert-sorted-array-to-binary-search-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given an integer array `nums` sorted in ascending order, convert it to a height-balanced binary search tree (any valid one is accepted).

## My Initial Intuition

Choose the middle element as the root so the left and right sides would have similar sizes, then do the same recursively for the left and right halves.

## Brute Force

Insert every element from the sorted array into a BST one by one. This keeps the BST property, but because the numbers are inserted in increasing order, the tree becomes completely skewed like a linked list instead of remaining balanced. 
Height: O(n), so insertion takes O(n) each in the worst case, for a total of O(n²).

## Key Insight

The middle element naturally splits the sorted array into values smaller than the root and values larger than the root, satisfying the BST property. Choosing the middle also keeps the left and right subtree sizes as equal as possible, producing a height-balanced tree. Since each half is still a sorted array, the same idea can be applied recursively.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Recursive helper `build(left, right)` operating on an index range into `nums`. Base case: if `left > right`, return `None` (empty range). Otherwise compute `mid = (left + right) // 2`, create `TreeNode(nums[mid])`, and recursively set `.left = build(left, mid - 1)` and `.right = build(mid + 1, right)`. Top-level call is `build(0, len(nums) - 1)`.

## Correctness Argument

- Base case: If left > right, the subarray is empty, so returning None correctly represents an empty subtree.
- Inductive step: Assume build correctly constructs balanced BSTs for all smaller subarrays. For the current subarray, the middle element is chosen as the root. All elements on the left are smaller than the root, and all elements on the right are larger because the array is sorted, so the BST property holds. By the induction hypothesis, the recursive calls correctly build balanced BSTs for the left and right halves. Attaching them to the root produces a height-balanced BST for the current subarray.

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

Mistakenly used TreeNode(mid) instead of TreeNode(nums[mid]). Mixed up the index with the element itself. The node's value should come from the array (nums[mid]), not the position (mid).

## How I Will Recognize This Pattern Next Time

Asks to build a balanced BST from a sorted sequence: choose the middle element as the root, then recursively build the left and right subtrees from the two halves.
