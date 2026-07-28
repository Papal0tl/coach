# Rubric

- Problem slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Can state that the first preorder value is always the current subtree's root | Correctly identified this unprompted while writing the code and in the blog's Initial Intuition. | met |
| Constraint analysis | Notices values are unique, which licenses a value->index map for O(1) split lookup | Used `.index()` on the (implicitly unique-valued) `inorder` array without needing to be told uniqueness was required; did not independently reach for a precomputed hash map. | partially met |
| Brute-force construction | Can produce a working slicing-based recursive solution (even if O(n^2)) | Submitted solution is exactly this; all 6 tests pass. | met |
| Pattern recognition | Connects this to prior index-range tree-building session (convert-sorted-array-to-binary-search-tree) | Not asked directly this session; carried forward as a note rather than tested live. | not tested |
| Invariant formulation | States precisely why left subtree must be built before right subtree (preorder consumption order) | Correctly derived, in words, why the left subtree occupies exactly the next `idx` values of `preorder`, before writing the corresponding code. Stated the general argument (not just the worked example) in the blog's Correctness Argument. | met |
| Complexity analysis | Distinguishes O(n^2) (slicing/linear search) from O(n) (pointer + hash map) and explains why | Named O(n^2) unprompted and precisely attributed it to `.index()` plus slicing costs per call; declined to implement the O(n) alternative. | met |
| Edge-case design | Covers single node, left-skewed, right-skewed, asymmetric split | Edge-case list was agent-filled and accepted unchallenged; not independently derived this session. | not independently tested |
| Debugging discipline | Runs code / traces concrete example rather than guessing | The off-by-one bug was caught via a guiding question before ever running the code, not by reading a runtime error — a new variant of the established empirical-debugging pattern. | met (different mechanism than usual) |
| Communication | English, precise invariant and complexity statements | All communication in English; invariant and complexity statements were both precise and unprompted. | met |

## Intervention Count

- Clarifying questions: 1 (trace the left/right sub-array slices by hand)
- Hints: 1 (does `inorder[idx:]` still contain the root value?)
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Strong session overall. The algorithmic reasoning (root-from-preorder-first, split-via-inorder-search, left-subtree-size determines the preorder split point) was correct and stated precisely in words before either bug occurred — both bugs that followed were pure code-translation slips, not reasoning gaps, and the second was caught proactively via a guiding question rather than by running broken code. Complexity analysis was volunteered accurately and unprompted. The session's one coaching-relevant event was in the blog: the user pushed back on including one of the two real bugs in Mistakes Made, arguing it was an intentional placeholder rather than a wrong attempt — a fair, evidence-backed distinction, accepted as valid rather than treated as evasion. No unresolved gaps; ready to archive.
