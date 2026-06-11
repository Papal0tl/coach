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

**Turn 2 — towards decomposition:**  
User identified n(n-1) multiplications. Responded correctly. Led through tracing the table to surface the left×right decomposition. User confirmed the pattern holds for all rows after a worked trace.

**Turn 3 — two-pass structure:**  
User wrote the left pass correctly on the first attempt (exclusive prefix, running variable, stored before multiply). Right pass had two bugs: `answer[j] = right` (overwrite) and `right *= nums[i]` (wrong loop variable). Both fixed after one targeted hint each. Final solution correct on all test cases including zeros and negatives.

**Turn 4 — invariant articulation:**  
After solution was confirmed, user stated the invariant precisely when asked: "answer[j] holds the product of all elements to the left of index j." Correct, unprompted.

**Blog:**  
One revision needed — Key Insight section described mechanics without naming the invariant explicitly; Mistakes section omitted the wrong-variable bug. Both corrected on first revision request.

**Outcome:**  
Correct O(n) time, O(1) extra space solution. First exposure to prefix/suffix product pattern. Not an independent solve — decomposition reached via guided tracing. Recovery from bugs was prompt once hinted.
