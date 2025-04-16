from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        pairs = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            pairs += count[nums[right]] - 1  # Add new pairs formed

            while pairs >= k:  # Shrink window when condition is met
                result += len(nums) - right  # Count valid subarrays
                count[nums[left]] -= 1
                pairs -= count[nums[left]]  # Remove pairs from shrinking window
                left += 1

        return result
