import math
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        # Helper function to check rotations for a specific target value x
        def check(x: int) -> int:
            rotations_top = 0
            rotations_bottom = 0
            for i in range(n):
                # If target x is not present in the current domino, it's impossible
                if tops[i] != x and bottoms[i] != x:
                    return float('inf') # Use infinity to signal impossibility

                # Count rotations needed to make tops row equal to x
                elif tops[i] != x:
                    rotations_top += 1
                # Count rotations needed to make bottoms row equal to x
                elif bottoms[i] != x:
                    rotations_bottom += 1
                # If tops[i] == x and bottoms[i] == x, no rotation count needs
                # to be incremented for either target row (top or bottom).

            # Return the minimum rotations needed to make either top or bottom row x
            return min(rotations_top, rotations_bottom)

        # Check rotations for the two potential target values
        rotations1 = check(tops[0])
        rotations2 = check(bottoms[0])

        # Find the minimum of the two checks
        min_rotations = min(rotations1, rotations2)

        # If min_rotations is infinity, it means neither target worked
        if min_rotations == float('inf'):
            return -1
        else:
            return min_rotations

# Example Usage (Optional)
# sol = Solution()
# tops1 = [2,1,2,4,2,2]
# bottoms1 = [5,2,6,2,3,2]
# print(f"Example 1: {sol.minDominoRotations(tops1, bottoms1)}") # Output: 2

# tops2 = [3,5,1,2,3]
# bottoms2 = [3,6,3,3,4]
# print(f"Example 2: {sol.minDominoRotations(tops2, bottoms2)}") # Output: -1
