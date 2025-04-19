from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Sorting the array to use binary search
        count = 0
        n = len(nums)

        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1, n)
            count += right - left

        return count
