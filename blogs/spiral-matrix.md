# Spiral Matrix (LC 54)

## Problem Summary
Given an m×n matrix, return all elements in spiral order (right → down → left → up, peeling inward layer by layer).

## Initial Intuition
Ssimulate the actual movement: go right, then down, then left, then up, and repeat. However, instead of tracking every visited cell with a set, I can shrink the valid area after finishing each side.

## Brute Force
Keep a visited set and move step by step in four directions. Whenever the next cell is out of bounds or already visited, change direction. This works, but it needs extra space to remember which cells were visited.

## Key Insight
The matrix can be viewed as layers. After finishing the top row, right column, bottom row, and left column, that outer layer is done. So we can move the four boundaries inward: top, right, bottom, and left. This avoids using a visited set.

## Final Algorithm
Maintain four boundaries: top, bottom, left, right.
While top ≤ bottom and left ≤ right:
  1. Traverse right along row `top`; top += 1
  2. Traverse down along col `right`; right -= 1
  3. If top ≤ bottom: traverse left along row `bottom`; bottom -= 1
  4. If left ≤ right: traverse up along col `left`; left += 1

## Correctness Argument
The algorithm always visit the current outer layer in spiral order. After one side is visited, its boundary is moved inward, so those elements will never be visited again.
The two guards are necessary because the remaining area may become a single row or a single column. If top > bottom, there is no bottom row left to traverse. If left > right, there is no left column left to traverse. These checks prevent adding the same row or column twice.

## Complexity
- Time: O(m × n) — every element visited exactly once.
- Space: O(1) auxiliary (output list not counted).

## Edge Cases
- 1×1: single element collected in step 1; steps 2–4 are empty.
- Single row (m=1): after step 1, top > bottom; guards block steps 3 and 4.
- Single column (n=1): after step 2, left > right; guards block steps 3 and 4.

## Mistakes Made
Wrote right += 1 after traversing the right column. The boundary should move inward, so the correct update is right -= 1.

Forgot the guards if top <= bottom and if left <= right. This caused the last row or last column to be traversed twice when the remaining matrix had only one row or one column.

First thought I needed a visited set to avoid revisiting cells. Later realized the four boundaries already guarantee that every element is visited exactly once.

## How to Recognize This Pattern Next Time
Use shrinking-boundary simulation when the problem asks you to traverse a 2D grid layer by layer from the outside inward.
