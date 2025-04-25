from collections import Counter
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Preprocess the nums array to mark if nums[i] % modulo == k
        marks = [1 if num % modulo == k else 0 for num in nums]
        
        # Create prefix sum
        prefix_sum = 0
        count_map = Counter()
        count_map[0] = 1  # Initialize for the case where prefix_sum itself satisfies condition
        
        result = 0
        
        for mark in marks:
            prefix_sum += mark
            # Check the required previous prefix sum to satisfy the condition
            target = (prefix_sum - k) % modulo
            result += count_map[target]
            # Record the current prefix_sum modulo for further computations
            count_map[prefix_sum % modulo] += 1
        
        return result
