# Rubric: Lowest Common Ancestor of a Binary Tree

## Skills to Observe

- **Brute-force construction**: does the user reach for "find both root-to-node paths, then compare them" as a first correct baseline?
- **Pattern recognition (new)**: bottom-up recursive search-and-merge for *two* targets is untested in this arc. Distinct from LC 101 (pair-comparison of two nodes at the same call) and from every prior single-target recursive shape (visit, combine, mutate, build, validate, rank-extract, path-sum). Watch whether the "both non-None means split here" insight is reached independently.
- **Edge-case handling**: correctly treating a node as its own ancestor (checking `root is p or root is q` before recursing) rather than only detecting `p`/`q` at leaves or via value equality that could misfire on duplicate values (constraints guarantee unique values, but identity vs. equality is still worth watching, consistent with this user's `!=` vs `is not` history).
- **Invariant formulation**: can the user state precisely what a recursive call's return value *means* in each of the three cases (found both -> LCA, found one -> that node signaling "still searching for the other," found none -> None)?
- **Complexity analysis**: O(n) time / O(h) space for the optimal approach vs. the brute force's two path-finding passes.
- **Debugging discipline**: if bugs occur, are they self-caught before running, or resolved via the established run-and-read-the-error preference?

## Not Yet Scored

- Problem restatement
- Constraint analysis
- Test design (agent writes tests in this workflow)

## Notes

This is the fifteenth tree-arc session and the first requiring simultaneous
search for two distinct target nodes with a bottom-up merge decision at every
level. The closest prior sessions are LC 101 (pair-of-nodes recursion, but a
*comparison*, not a *search*) and LC 437 (single accumulator threaded
downward, not two independent search targets merged upward). Expect this to
test whether "recursion can return a signal richer than a plain
found/not-found boolean" (here: found-nothing / found-one-of-them /
found-the-answer) transfers cleanly from LC 543's return-height-track-diameter
side-channel pattern.
