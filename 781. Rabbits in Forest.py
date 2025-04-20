from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        
        for answer, freq in count.items():
            group_size = answer + 1
            num_groups = (freq + group_size - 1) // group_size  # Ceiling division to ensure groups are full
            total_rabbits += num_groups * group_size
        
        return total_rabbits
