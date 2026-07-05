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

(to be filled in after the attempt is complete)
