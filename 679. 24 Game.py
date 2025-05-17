import itertools

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def can_reach_24(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]

                    # Try all four operations
                    if can_reach_24(remaining + [a + b]):
                        return True
                    if can_reach_24(remaining + [a - b]):
                        return True
                    if can_reach_24(remaining + [b - a]):
                        return True
                    if can_reach_24(remaining + [a * b]):
                        return True
                    if b != 0 and can_reach_24(remaining + [a / b]):
                        return True
                    if a != 0 and can_reach_24(remaining + [b / a]):
                        return True
            return False

        for p in itertools.permutations(cards):
            if can_reach_24(list(p)):
                return True
        return False
