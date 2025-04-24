from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Count distinct elements in the entire array
        total_distinct = len(set(nums))
        
        count = 0
        n = len(nums)
        
        # Check each subarray
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                # If distinct count matches total distinct count
                if len(seen) == total_distinct:
                    count += 1
        return count
