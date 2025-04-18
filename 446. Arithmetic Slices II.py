from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count = 0
        dp = [defaultdict(int) for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                dp[i][diff] += count + 1
                total_count += count

        return total_count
