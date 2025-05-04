from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize the domino by sorting
            pairs += count[key]  # Every previous occurrence forms a valid pair
            count[key] += 1
        
        return pairs
