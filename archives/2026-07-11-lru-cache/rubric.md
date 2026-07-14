# Rubric

- Problem slug: `lru-cache`
- Archive path: `archives/2026-07-11-lru-cache/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Identify this as a design problem needing O(1) get/put, not a single-function transform | First draft (unprompted) defined a standalone `Node` class and a `self.cache` dict from the start — correctly scoped this as a stateful class design, not a single-function transform, on the very first attempt. | met |
| Constraint analysis | Recognize the O(1) requirement rules out a plain dict-only or list-only approach for tracking recency | Blog Key Insight states precisely: hash map alone has no O(1) recency tracking, linked list alone has no O(1) key lookup. | met |
| Brute-force construction | Describe an O(n)-per-op approach (e.g. dict + separate order list with linear search/removal) | Blog Brute Force: dict + list, correctly identifies O(n) cost of removing an arbitrary key from the list. | met |
| Pattern recognition | Reach hash map (key -> node) + doubly linked list without being told; first design-problem session in the arc, first hash-map-of-mutable-nodes composition | First draft independently reached for `Node()` + `self.cache` dict with no hint — first design-problem session and first hash-map-of-mutable-linked-list-nodes composition in the arc, reached cold. | met, strong |
| Invariant formulation | State precisely what "recency order" means as a list position invariant (front = MRU, back = LRU), and that every touch moves a node to the front | Blog Correctness Argument states the invariant precisely: list always ordered MRU-to-LRU, every touch moves the node to front, so `tail.prev` is always safe to evict. | met |
| Complexity analysis | State O(1) average time / O(capacity) space for the final design | Complexity section was agent-filled and accepted without revision; not independently re-derived by the user this session (no verbal complexity question was asked). | met (agent-filled, user-confirmed only) |
| Edge-case design | Handle capacity 1, get on a missing key, put updating an existing key (value + recency refresh, no eviction), eviction exactly at the capacity boundary | `attempt.py` handles all of these correctly with no special-casing (sentinel head/tail design generalizes cleanly); confirmed by all 6 reference tests passing, including `test_capacity_one` and `test_eviction_at_exact_capacity_boundary`. | met |
| Debugging discipline | Diagnose and fix bugs efficiently, ideally by running code and reading real output rather than only mental tracing | Same mechanical bug (bare `cache` instead of `self.cache`) recurred across two drafts (once in `get` only, then in both `get` and `put`), not self-caught before running either time. Resolved in one round each time via `NameError` from actually running the code — consistent with this user's established empirical-debugging preference. No logic bugs at all this session; both slips were name-scoping only. | met, with a repeated mechanical slip |
| Communication | Write an accurate, precise blog matching the actual session history | Correctness Argument, Key Insight, Brute Force, and How I Will Recognize This Pattern sections were all precise and accurate on first submission, zero revisions needed. Mistakes Made described genuine conceptual clarifications (what "most recently used" means, why dict-alone/list-alone fail, update-vs-insert distinction) rather than the two literal git-history bugs (the repeated `self.cache` `NameError`, the first draft's incomplete `__init__`) — a new variant of the long-tracked Mistakes-section gap: substitution rather than fabrication or omission-under-load. Flagged as optional in review; user declined the addition ("no need to write these two bugs"), the first time this specific gap was surfaced as optional (not required) and then explicitly waived. | met, with a noted gap |

## Intervention Count

- Clarifying questions: 1 (first draft: what should `__init__`'s `key`/`value` represent, and where is `Node` defined)
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 1 (ran the code directly and pointed at the resulting `NameError` rather than naming the `self.cache` fix)

## Closeout Assessment

Strong first design-problem session. Reached the full hash-map + doubly-linked-list pattern cold, with zero structural hints — the only intervention was one clarifying question on the very first (incomplete) draft and one code-level nudge (run-it-and-read-the-traceback) for a repeated mechanical `self.` scoping slip. Zero logic bugs across the whole session. Blog is accurate and precise everywhere except Mistakes Made, which substitutes real conceptual struggles for the literal bugs — a milder, non-fabricating variant of the long-running Mistakes-section pattern tracked in `profile/user_profile.md`. Ready to archive.
