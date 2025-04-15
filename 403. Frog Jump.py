from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Create a set for quick lookup of stone positions
        stone_positions = set(stones)
        # Memoization dictionary to store already computed results
        memo = {}

        def dfs(position, jump):
            if (position, jump) in memo:
                return memo[(position, jump)]

            # If we've reached the last stone, return True
            if position == stones[-1]:
                return True
            
            # Try all possible jumps: k-1, k, k+1
            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump > 0 and position + next_jump in stone_positions:
                    if dfs(position + next_jump, next_jump):
                        memo[(position, jump)] = True
                        return True
            
            memo[(position, jump)] = False
            return False
        
        # The first jump must be exactly 1 unit
        return dfs(1, 1) if 1 in stone_positions else False
