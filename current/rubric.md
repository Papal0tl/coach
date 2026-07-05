# Rubric — Linked List Cycle (LC 141)

## Skill Targets

- Recognize that a naive "compare to head" or index-based approach doesn't work on a linked list (no random access, unknown length, cycle means no natural end).
- Reach a correct cycle-detection approach:
  - Hash set of visited nodes (O(n) space), or
  - Fast/slow pointer (Floyd's), O(1) space.
- Correctly implement pointer movement without off-by-one/null-dereference errors (`fast.next` and `fast.next.next` guard checks).
- State the loop invariant / termination argument: why fast and slow must meet if a cycle exists, and why fast reaching `None` proves no cycle.
- State time and space complexity.

## Evaluation

(to be filled in after the attempt is complete)
