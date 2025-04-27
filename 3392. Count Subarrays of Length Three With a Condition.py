from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Counts the number of contiguous subarrays of length 3 such that
        the sum of the first and third numbers equals exactly half of the second number.

        Args:
            nums: A list of integers.

        Returns:
            The count of such subarrays.
        """
        count = 0
        n = len(nums)

        # If the array has fewer than 3 elements, no such subarray can exist.
        if n < 3:
            return 0

        # Iterate through all possible starting indices for a subarray of length 3.
        # The loop goes from index 0 up to n-3 (inclusive).
        # range(n - 2) correctly covers indices 0, 1, ..., n-3.
        for i in range(n - 2):
            first = nums[i]
            second = nums[i+1]
            third = nums[i+2]

            # Check the condition: nums[i] + nums[i+2] == nums[i+1] / 2
            # Rewrite to avoid potential float issues: 2 * (nums[i] + nums[i+2]) == nums[i+1]
            if 2 * (first + third) == second:
                count += 1

        return count
