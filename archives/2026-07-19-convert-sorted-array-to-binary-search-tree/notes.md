# Session Notes

- Problem slug: `convert-sorted-array-to-binary-search-tree`
- Archive path: `archives/2026-07-19-convert-sorted-array-to-binary-search-tree/`

## Agent Preparation

- Pattern: recursive divide-and-conquer over an array index range — seventh tree session in the arc, and the first that *builds* a tree from an array rather than traversing or transforming an existing tree. Structurally closer to sort-list's split/recurse/merge shape (linked-list arc) than to any prior tree session.
- Key insight: picking the *middle* index of each sorted sub-range as the subtree root is what guarantees height-balance — everything left of the middle is smaller and everything right is larger (already true from sorted order, so no comparisons are needed), and a middle split keeps the two recursive subtrees within one node of each other in height.
- Invariant or state: a call on range `[lo, hi]` returns the root of a valid, height-balanced BST over exactly `nums[lo..hi]`, or `None` when `lo > hi`.
- Complexity target: O(n) time (each element becomes one node), O(log n) additional space for the recursion stack (tree height is O(log n) from the balanced split), not counting the O(n) output tree.

## Reference Solution Summary

Recursive helper `build(lo, hi)` on index bounds into `nums`. Base case `lo > hi` returns `None`. Otherwise compute `mid = (lo + hi) // 2`, create `TreeNode(nums[mid])`, recurse for `.left = build(lo, mid - 1)` and `.right = build(mid + 1, hi)`. Top-level call is `build(0, len(nums) - 1)`.

## Edge Cases

- Single element (`[1]`) -> single node, no children.
- Even-length array -> `mid` rounds down (integer division), so the left subtree gets one fewer element than the right; still balanced (heights differ by at most 1). Either floor or ceiling mid is accepted by the judge since multiple valid trees exist.
- Two elements (`[1, 3]`) -> a specific mid-selection choice determines whether the root is the smaller or larger value; both are valid outputs.
- Larger inputs (up to 10^4 per constraints) -> recursion depth stays O(log n), no stack-depth concern.

## User-Facing Takeaways

- This is the first tree session that starts from an array instead of an existing tree — watch whether the divide-and-conquer index-range recursion (a shape already exercised in sort-list, LC 148) transfers cleanly, or whether the "no explicit comparisons needed because the input is already sorted" aspect causes hesitation.
- Off-by-one risk is concentrated in the `mid` calculation and the `build(lo, mid - 1)` / `build(mid + 1, hi)` boundary exclusions — a good area to watch for a first-draft bug given the arc's history of boundary/index bugs in array problems.

## Follow-Up Candidates

- Convert Sorted List to Binary Search Tree (LC 109): same idea, but without random access to the middle element — tests whether the array-index approach is understood deeply enough to adapt when direct indexing isn't available.

## Coaching Log

- First draft (commit `2b47467`): the full divide-and-conquer shape — `build(left, right)` helper, `left > right` base case, `mid = (left + right) // 2`, `TreeNode(nums[mid])`, and recursive `.left`/`.right` assignment with correctly excluded boundaries (`mid - 1`, `mid + 1`) — matches the reference solution structurally, written unprompted. Strong first-attempt transfer of the sort-list-style split/recurse shape to a build-a-tree-from-array context. One bug: `TreeNode` is referenced but never defined or imported in `attempt.py`, so running it will raise a `NameError`. Consistent with the established empirical-debugging preference, prompted to run the file rather than pointing out the missing class directly.
- Fix (commit `e09dac1`): after being shown the real `NameError: name 'TreeNode' is not defined` traceback, added the standard `TreeNode` class definition directly above `Solution`, self-fixed with no further hints. All 6 reference tests pass (inorder-matches-sorted-input + height-balanced checks). Zero logic bugs this session so far — the only issue was the missing class definition, resolved via the established run-it-and-read-the-error approach.
