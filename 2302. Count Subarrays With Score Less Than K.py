import math
from typing import List

class Solution:
  """
  Solves the LeetCode problem "Count Subarrays With Score Less Than K".

  The score of an array is defined as the product of its sum and its length.
  This class provides a method to count the number of non-empty subarrays
  of a given array `nums` whose score is strictly less than a given integer `k`.
  """
  def countSubarrays(self, nums: List[int], k: int) -> int:
    """
    Counts the number of subarrays with score less than k using a sliding window approach.

    Args:
      nums: A list of positive integers.
      k: An integer threshold for the score.

    Returns:
      The total number of non-empty subarrays of nums whose score (sum * length) is strictly less than k.
    """
    count = 0
    current_sum = 0
    left = 0
    n = len(nums)

    # Iterate through the array with the right pointer of the sliding window
    for right in range(n):
      # Expand the window by including the element at the right pointer
      current_sum += nums[right]

      # Shrink the window from the left side as long as the score condition is violated
      # The score of the current window [left, right] is current_sum * (right - left + 1)
      # We need current_sum * (right - left + 1) < k
      # So, we shrink while current_sum * (right - left + 1) >= k
      # Also ensure left pointer doesn't exceed right pointer during checks within the loop
      while left <= right and current_sum * (right - left + 1) >= k:
        # Remove the element at the left pointer from the sum
        current_sum -= nums[left]
        # Move the left pointer to the right
        left += 1

      # After the while loop, the window [left, right] satisfies the score condition (score < k).
      # Any subarray ending at 'right' and starting at an index 'i' such that left <= i <= right
      # will also have a score less than k. This is because both the sum and length
      # of such subarrays are less than or equal to the sum and length of the window [left, right].
      # The number of such valid subarrays ending at 'right' is (right - left + 1).
      # If the initial single element nums[right] itself caused the score >= k,
      # the while loop would have incremented 'left' past 'right' (left = right + 1),
      # resulting in (right - (right + 1) + 1) = 0 subarrays being added, which is correct.
      count += (right - left + 1)

    return count
