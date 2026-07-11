# Session Notes

- Problem slug: `merge-k-sorted-lists`
- Archive path: `archives/2026-07-10-merge-k-sorted-lists/`

## Agent Preparation

- Pattern: k-way merge via a min-heap (also solvable via divide-and-conquer pairwise merge, or brute-force collect-and-sort).
- Key insight: at any point, the next smallest overall element must be the head of one of the k lists (since each list is individually sorted). A min-heap holding at most one "current head" per list gives that minimum in O(log k) instead of O(k) per pop.
- Invariant or state: the heap always contains at most one node per still-active list — specifically each list's current unconsumed head. Popping the minimum and pushing its `.next` (if any) maintains this.
- Complexity target: O(N log k) time (N = total nodes across all lists, k = number of lists), O(k) extra space for the heap (output list reuses input nodes).

## Reference Solution Summary

Push `(val, index, node)` for each list's head into a heap (index used purely as a heap tiebreaker so `ListNode` objects are never compared). Repeatedly pop the minimum, append it to a dummy-headed result list, and push its successor back onto the heap if one exists.

## Edge Cases

- `lists = []` → return `None`.
- `lists = [None]` / list of all `None`s → return `None`.
- Single non-empty list → return it unchanged (heap degenerates to size 1).
- Mix of empty and non-empty lists.
- Duplicate values across lists (heap tiebreak on index must not compare `ListNode`s directly, and equal values must both come out — order between equal values is not specified by the problem but must not crash or drop nodes).
- Negative and boundary values (`-10^4`, `10^4`).
- Large k with short lists vs. small k with one long list (motivates why O(N log k) beats brute-force O(Nk)).

## User-Facing Takeaways

- This generalizes merge-two-sorted-lists (2026-07-05) from k=2 to arbitrary k.
- Natural first instinct is likely a pairwise-merge loop (reduce k lists two at a time, similar structurally to sort-list's merge step) — that is a valid O(N log k) divide-and-conquer alternative. Watch whether the user reaches for that or for collect-all-then-sort (O(N log N), also valid but not pattern-matching to "merge").
- Heap/priority-queue as a way to repeatedly extract a running minimum across multiple sorted sources has not been used yet in this arc — first opportunity to observe whether `heapq` is reached for independently.

## Follow-Up Candidates

- Ask for the divide-and-conquer pairwise-merge alternative and compare its complexity/constant-factor tradeoffs to the heap approach.
- Ask why comparing raw `ListNode` objects in the heap would fail on tie (Python has no default `<` for arbitrary objects) — connects to the index-tiebreak trick.

## Coaching Log

### First attempt (sequential pairwise merge, folds `lists` one at a time into `merge`)

- Approach chosen: sequential fold — reduce `merge` (accumulated result) against each `cur_list` in turn using a dummy-node merge loop. Valid O(Nk) strategy, structurally close to merge-two-sorted-lists's core loop, reused unprompted.
- Bug: inside the merge loop, the code does `cur.val = list1.val; cur = cur.next; list1 = list1.next` — copying a value into the current node and then advancing `cur` via `cur.next`, but `cur.next` was never pointed at a new node, so `cur.next` is always `None` (from `dummy = ListNode(0)`). This makes `cur` become `None` after the very first assignment inside the loop, crashing with `AttributeError: 'NoneType' object has no attribute 'val'` on the second inner-loop iteration of the second outer-loop pass onward. Confirmed empirically with the example input: crashes exactly at `cur.val = list2.val` when merging list 2 (`[1,4,5]`) with list 3... actually crashes merging accumulated `merge=[1,4,5]` against `cur_list=[1,3,4]`.
- This is a departure from the technique the user has used successfully in every prior linked-list session (merge-two-sorted-lists, add-two-numbers, etc.): attach the actual existing node (`cur.next = list1; cur = cur.next`) rather than copy `.val` into a pre-existing dummy chain. Worth watching whether they self-diagnose by tracing `cur` across iterations, or need the invariant ("cur.next must point at a real node before you advance into it") surfaced directly.
- Intervention used: asked user to run the code themselves and trace what `cur` is bound to right before the crash (step 1 of default intervention order — clarifying/trace request). No hint given yet.
- Fix: on the very next turn, changed `cur.val = list1.val` / `cur.val = list2.val` to `cur.next = list1` / `cur.next = list2`, correctly reattaching the actual node instead of copying its value — self-corrected from a single trace prompt with no further hint needed. Verified against all 8 local cases (basic merge, empty `lists`, all-`None` `lists`, single list, mixed empty/non-empty, all-duplicate values, negatives) — all pass. This is the same node-reattachment technique from every prior linked-list session; the bug was a one-off slip (copying `.val` into a dummy chain) rather than a gap in understanding the dummy-node pattern itself.
- Correctly stated divide-and-conquer is O(N log k) vs. sequential fold's O(Nk) on the first ask. First attempt to explain *why* was vague ("each merge only compares two heads at a time, k stays linear") and didn't isolate the log k factor, so followed up with a concrete trace: k=8 lists, count rounds and per-round work. User correctly derived rounds = log2(k) and that each round touches all N elements (O(N) per round → O(N log k) total). Then, prompted to trace the sequential fold the same way, correctly reasoned that the accumulated list keeps growing across the k-1 merges, so per-merge cost grows and the total sums to O(Nk) — fully self-derived once broken into concrete counting steps, no direct explanation needed. Complexity analysis rubric target met via guided trace rather than on the first unprompted try.
- Minor cleanup edit (no logic change): `if lists is None` → `if not lists` (also short-circuits on empty `lists`, previously relied on the for-loop over an empty list falling through to `return merge` = `None` — same result, more direct); and reordered `cur = cur.next` to come after `list1 = list1.next` instead of before. Verified the reorder is a genuine no-op: `cur.next` was already bound to the list1/list2 node object before `list1`/`list2` gets reassigned, so advancing the loop variable first doesn't change what `cur.next` points to. All 8 cases still pass. Reads as pointer-aliasing reasoning consistent with swap-nodes-in-pairs (2026-07-06), applied here without being asked.
