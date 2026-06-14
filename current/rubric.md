# Rubric — set-matrix-zeroes

## Skill Targets

- **Two-pass discipline**: collects all zero positions before mutating anything.
- **Space awareness**: reaches O(m+n) set-based solution; bonus for O(1) marker approach.
- **Edge-case sensitivity**: handles zeros in the first row/col without corruption.

## Acceptance Criteria

- Correct output on both provided examples.
- Does not cascade-zero based on zeros introduced during the same pass.
- Time: O(mn). Space: O(m+n) is baseline; O(1) is follow-up.

## Observations to Watch

- Whether the user notices the cascade-corruption risk immediately or only after tracing.
- Whether the user reaches for sets vs. a list of (row, col) pairs.
- Whether the user attempts the O(1) approach unprompted.
- Whether the user handles the first-row/col edge case correctly in the O(1) approach.
