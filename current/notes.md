# Session Notes — Product of Array Except Self

## Problem Analysis

**Pattern:** Prefix/suffix product — two-pass scan

**Key insight:**  
For any index i, `answer[i]` = (product of everything to the LEFT of i) × (product of everything to the RIGHT of i).  
Neither half uses `nums[i]` itself. Compute the two halves in separate passes without division.

**Invariant:**  
After the left pass, `answer[i]` holds the product of `nums[0..i-1]` (the prefix product *excluding* i).  
After the right pass, `answer[i]` holds that prefix product multiplied by the suffix product `nums[i+1..n-1]`.  
Both passes maintain a single running variable (prefix / suffix), so no extra array is needed.

**Complexity:**  
- Time: O(n) — two linear passes  
- Space: O(1) extra (output array is excluded per LeetCode convention)

**Edge cases:**  
- Single zero in `nums`: all positions except the zero index produce 0 in the output; the zero-index position gets the product of all others.  
- Two or more zeros: the entire output is 0.  
- Negative numbers: sign is handled naturally by multiplication; no special case needed.  
- Minimum length (n = 2): both passes work correctly.

## Coaching Log

**Turn 1 — brute force attempt:**  
User wrote a correct O(n²) nested loop: outer loop over i, inner loop over j skipping i. Logic and output accumulation are correct. The constraint violation is time complexity (O(n²)) — the problem requires O(n). Intervention: ask user to count operations to surface the complexity issue without naming it directly.
