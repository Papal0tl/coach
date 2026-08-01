# Blog Review: Binary Tree Maximum Path Sum

- Problem slug: `binary-tree-maximum-path-sum`
- Archive path: `archives/2026-07-31-binary-tree-maximum-path-sum/`

## Correctness

Algorithm description is correct and matches the working `attempt.py` / `agent_solution.py`. Key Insight correctly states the core distinction: a node's contribution to the tracked best may use both children, but the value returned to the parent may use only one. Correctness Argument is directionally right (describes what `gain` and `self.res` each do) but stays at the mechanism-description level rather than arguing exhaustiveness — it doesn't explicitly say *why* every possible path is guaranteed to be checked (every path has a unique topmost/bend node, and that node's `self.res` update is exactly where it gets counted). Not blocking, but worth a mental note for next time a correctness argument is written.

## Missing Concepts

None major. Complexity and edge cases (agent-filled) are accurate and match the reference solution and test suite.

## Clarity

Concise throughout, no padding. Brute Force section is thinner than most prior sessions' ("too many possible paths" without naming a concrete O(n^2) approach, e.g. recomputing a downward-path sum rooted at every node), but still communicates the right intuition (exhaustive path enumeration is too slow).

## Transfer Readiness

Good. "How I Will Recognize This Pattern Next Time" correctly generalizes the return-vs-tracked-best split as the reusable idea, independent of this specific problem.

## Required Revisions

- **Mistakes I Made is incomplete.** It lists the three logic-level issues (missing `root.val` in the tracked-best update, conflating the returned value with the tracked best, and the one-side-only return) but omits two real bugs from the commit history: (1) the first draft defined `dfs` but never called `dfs(root)`, so the function always returned `-inf`; (2) the first draft had a `sef.res` typo (should be `self.res`). This is a recurring gap in this arc — Mistakes I Made sections have repeatedly omitted mechanical/syntax-level bugs in favor of only the conceptual ones.
  - **Declined.** User explicitly chose not to add these two, closing the session with only the conceptual bugs documented.

## Agent Assessment

Strong session. The recursive shape and the negative-branch clamping transferred with zero prompting. The real bug — conflating "value returned to caller" with "value tracked as running best" — is the same family of bug as diameter-of-binary-tree (2026-07-17), but this time it was resolved in three self-driven edits with a single trace prompt, no scoping/`nonlocal` confusion. Ready to transfer this return-vs-tracked-best pattern to future problems.
