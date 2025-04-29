import math
from typing import List

class Solution:
  """
  Solves the LeetCode problem: Count Subarrays Where Max Element Appears At Least K Times.
  Finds the number of contiguous subarrays where the globally maximum element
  of the input array `nums` occurs at least `k` times.
  """
  def countSubarrays(self, nums: List[int], k: int) -> int:
    """
    Counts valid subarrays using a sliding window approach.

    Args:
      nums: A list of integers. Constraints: 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^6.
      k: The minimum required frequency of the maximum element in a subarray. Constraint: 1 <= k <= 10^5.

    Returns:
      The total number of subarrays satisfying the condition. The result fits in a 64-bit integer.
    """
    n = len(nums)
    # Per constraints, n >= 1, so no need to check for empty list explicitly.

    # 1. Find the maximum value in the input array. O(N)
    # Constraints state 1 <= nums[i], so max_val will be at least 1.
    max_val = 0
    for x in nums:
        if x > max_val:
            max_val = x
    # Or simply: max_val = max(nums)

    ans = 0           # Initialize the count of valid subarrays (can be large, up to O(N^2))
    left = 0          # Initialize the left pointer of the sliding window
    max_val_count = 0 # Initialize the count of max_val within the window [left, right]

    # 2. Iterate through the array with the right pointer of the sliding window.
    for right in range(n):
        # Expand the window by including the element at the right pointer.
        # If the current element is the maximum value, increment its count in the window.
        if nums[right] == max_val:
            max_val_count += 1

        # 3. Shrink the window from the left while maintaining the condition (count >= k).
        # While the window [left, right] contains at least k occurrences of max_val:
        # This means the current window is "valid".
        # Crucially, any subarray that STARTS at the current `left` index and ENDS at `right`
        # or any index AFTER `right` (i.e., right, right+1, ..., n-1) is guaranteed
        # to contain the `k` (or more) `max_val`s currently found in `[left, right]`.
        # The number of such possible ending points is `n - right`.
        # Therefore, the current `left` index, as a starting point, contributes `(n - right)`
        # valid subarrays to our total count.
        while max_val_count >= k:
            ans += (n - right)

            # Now, try to shrink the window from the left to find the *next* possible
            # valid starting point (`left + 1`).
            # If the element at the `left` pointer (which is about to be removed)
            # is the maximum value, we decrement the count for the window.
            if nums[left] == max_val:
                max_val_count -= 1
            
            # Move the left pointer one step to the right, effectively shrinking the window.
            left += 1
            # The loop will then re-evaluate the condition `max_val_count >= k` for the
            # new, smaller window `[left, right]`. If the condition still holds,
            # it means the *new* `left` index also contributes `(n - right)` valid subarrays,
            # and we add this contribution before shrinking further.

    # 4. Return the total accumulated count.
    return ans
