from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_value, max_value = 0, 0
        current = 0
        
        for diff in differences:
            current += diff
            min_value = min(min_value, current)
            max_value = max(max_value, current)
        
        possible_starts = (upper - lower) - (max_value - min_value) + 1
        return max(0, possible_starts)
