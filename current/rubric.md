# Rubric

- Problem slug: `lru-cache`
- Archive path: `archives/2026-07-11-lru-cache/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Identify this as a design problem needing O(1) get/put, not a single-function transform | — | pending |
| Constraint analysis | Recognize the O(1) requirement rules out a plain dict-only or list-only approach for tracking recency | — | pending |
| Brute-force construction | Describe an O(n)-per-op approach (e.g. dict + separate order list with linear search/removal) | — | pending |
| Pattern recognition | Reach hash map (key -> node) + doubly linked list without being told; first design-problem session in the arc, first hash-map-of-mutable-nodes composition | — | pending |
| Invariant formulation | State precisely what "recency order" means as a list position invariant (front = MRU, back = LRU), and that every touch moves a node to the front | — | pending |
| Complexity analysis | State O(1) average time / O(capacity) space for the final design | — | pending |
| Edge-case design | Handle capacity 1, get on a missing key, put updating an existing key (value + recency refresh, no eviction), eviction exactly at the capacity boundary | — | pending |
| Debugging discipline | — | — | pending |
| Communication | — | — | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending.
