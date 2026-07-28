# Session Notes

- Problem slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

## Agent Preparation

- Pattern: Recursive tree construction from two traversal orders (divide-and-conquer, index-range recursion).
- Key insight: The first element of `preorder` is always the root of the (sub)tree currently being built. That value's position in `inorder` splits the remaining `inorder` range into the left subtree's values (everything before it) and the right subtree's values (everything after it). A hash map from value -> inorder index turns that split-point lookup into O(1); a single shared, monotonically-advancing pointer into `preorder` (rather than slicing) avoids O(n) array copies per call.
- Invariant or state: At each recursive call `build(left, right)`, the value at the current `preorder` pointer position is exactly the root of the subtree whose in-order values occupy `inorder[left..right]`. Because `preorder` is a full root-first walk (root, then all of left subtree, then all of right subtree) and the pointer only ever advances, calling `build(left, mid-1)` before `build(mid+1, right)` consumes preorder values in the exact order the tree was walked.
- Complexity target: O(n) time, O(n) space (index map + recursion stack, worst case O(n) depth on a skewed tree).

## Reference Solution Summary

Build an `inorder` value -> index map once. Use a single instance-level pointer (`self.pre_pos`) into `preorder` that always points at the next unconsumed preorder value. Recursive helper `build(left, right)` on the `inorder` index range: base case `left > right` returns `None`; otherwise take `preorder[self.pre_pos]` as the root, advance the pointer, look up `mid = index_of[root_val]` in `inorder`, then recurse left on `(left, mid-1)` and right on `(mid+1, right)` *in that order* (left subtree's preorder values must be consumed before the right subtree's).

## Edge Cases

- Single node (`preorder = [x]`, `inorder = [x]`).
- Left-skewed tree (every node has only a left child).
- Right-skewed tree (every node has only a right child).
- Root with only a left child, no right child (asymmetric split where `mid == right`).
- Balanced small tree (both subtrees non-trivial) to check the split logic isn't accidentally always one-sided.
- Constraint guarantees `preorder.length >= 1`, so an empty-tree/`None` root input is not part of the graded input space (though the recursion's base case still returns `None` for an empty sub-range).

## User-Facing Takeaways

- The problem is a divide-and-conquer / index-range recursion, close in spirit to `convert-sorted-array-to-binary-search-tree` (index-range recursion building a tree) but now driven by *two* traversal arrays instead of one sorted array, and the split point must be *found* (via `inorder`) rather than computed by a midpoint formula.
- The naming/order dependency (build left before right, because `preorder` is root-first-left-right) is the likely trickiest invariant to state precisely.

## Session Log

- First draft used the slicing approach (not the pointer + hash-map reference approach), correct algorithmic shape immediately: base case, root from `preorder[0]`, `idx = inorder.index(root.val)`.
- First bug: recursive calls `self.buildTree()` had no arguments at all. Asked to trace `preorder=[3,9,20,15,7]`, `inorder=[9,3,15,20,7]` by hand and state the left/right sub-array slices in words before touching code. User correctly derived all four slices unprompted: `preorder[1:idx+1]`/`inorder[:idx]` for left, `preorder[idx+1:]`/`inorder[idx+1:]` for right — including the general (not just this-example) reasoning that the left subtree always has exactly `idx` nodes.
- Second bug: when translating that reasoning into code, wrote `inorder[idx:]` for the right subtree (off by one, includes the root's own value). Caught after one guiding question ("does `inorder[idx:]` still contain the root value?"); self-corrected to `inorder[idx+1:]` immediately.
- Both bugs were mechanical translation slips (args omitted, one boundary off), not conceptual — the underlying algorithmic reasoning (stated in words) was correct both times before the code was written/fixed.
- All 6 reference tests pass using the slicing approach.

## Follow-Up Candidates

- Compare against the "slice preorder and inorder into subarrays" approach (simpler to write, but O(n^2) worst case from repeated slicing/searching) versus the O(n) pointer + hash-map approach.
- LC 106 (Construct Binary Tree from Inorder and Postorder Traversal) as a direct transfer test: postorder gives the root from the *end* instead of the start, and subtrees must be recursed right-before-left to keep pointer consumption order correct.
