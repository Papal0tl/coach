# Rubric — Linked List Cycle (LC 141)

## Skill Targets

- Recognize that a naive "compare to head" or index-based approach doesn't work on a linked list (no random access, unknown length, cycle means no natural end).
- Reach a correct cycle-detection approach:
  - Hash set of visited nodes (O(n) space), or
  - Fast/slow pointer (Floyd's), O(1) space.
- Correctly implement pointer movement without off-by-one/null-dereference errors (`fast.next` and `fast.next.next` guard checks).
- State the loop invariant / termination argument: why fast and slow must meet if a cycle exists, and why fast reaching `None` proves no cycle.
- State time and space complexity.

## Coaching Target

Given the user has twice declined the O(1)-space fast/slow follow-up after landing on a hash-set solution first (reverse-linked-list, palindrome-linked-list), this session's primary interest is whether they reach for fast/slow directly, or need the hash-set path exhausted first before considering it. Either path is acceptable for a correct first attempt; hint-only mode should nudge toward considering the space tradeoff explicitly rather than assuming it.

## Evaluation

- Reached hash-set (visited-node) solution first, zero bugs, correct on first attempt.
- Stated O(n) time / O(n) space correctly, unprompted.
- Named "fast and slow pointer" as the O(1)-space alternative without being shown it, when asked if one exists.
- Did not implement fast/slow in `attempt.py`, but wrote and reasoned through correct fast/slow code in the blog's Final Algorithm section (guard conditions, meeting-point check, and the two-case correctness argument all present and accurate). Verified independently: passes all reference tests.
- All rubric skill targets met, either in `attempt.py` or in the blog.
