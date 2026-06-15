# Rubric — set-matrix-zeroes

## Skill Targets

- **Two-pass discipline**: collects all zero positions before mutating anything.
- **Space awareness**: reaches O(m+n) set-based solution; bonus for O(1) marker approach.
- **Edge-case sensitivity**: handles zeros in the first row/col without corruption.

## Acceptance Criteria

- Correct output on both provided examples.
- Does not cascade-zero based on zeros introduced during the same pass.
- Time: O(mn). Space: O(m+n) is baseline; O(1) is follow-up.

## Observations (session 2026-06-15)

- Attempted O(1) approach immediately without prompting. ✓
- Did not attempt O(m+n) set solution first.
- Cascade-corruption bug not independently caught — required two trace prompts to identify.
- Variable swap not self-caught — required explicit hint about which dimension each loop scans.
- First-row/col edge case: understood structurally (saved two booleans, handled last) but introduced range(n)/range(m) error and variable swap in implementation.
- Blog: correctness argument solid on first draft. "How to Recognize" revised on first request with strong generalisation.
