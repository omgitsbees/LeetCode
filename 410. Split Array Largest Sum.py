from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            subarray_count = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num

                if subarray_count > k:
                    return False

            return True
        
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid  # Try minimizing max sum
            else:
                left = mid + 1  # Increase max sum limit

        return left  # Minimum largest sum achievable
