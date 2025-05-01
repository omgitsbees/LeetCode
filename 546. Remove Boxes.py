import sys
from functools import lru_cache
from typing import List

# Increase recursion depth limit for potentially deep recursion stacks
# sys.setrecursionlimit(2000) # Uncomment if needed, LeetCode usually has sufficient default depth

class Solution:
    """
    Solves the Remove Boxes problem using dynamic programming with memoization.
    """
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        Main function to initiate the DP calculation.

        Args:
            boxes: A list of integers representing the colors of the boxes.

        Returns:
            The maximum points obtainable by removing boxes according to the rules.
        """
        n = len(boxes)

        # lru_cache(None) provides memoization for the solve function.
        # It stores the results of solve(l, r, k) to avoid re-computation.
        @lru_cache(None)
        def solve(l: int, r: int, k: int) -> int:
            """
            Recursive helper function with memoization.

            Calculates the maximum points obtainable from the subarray boxes[l...r],
            assuming there are k boxes with the same color as boxes[r]
            immediately following the index r.

            Args:
                l: Left index of the current subarray.
                r: Right index of the current subarray.
                k: Count of boxes identical to boxes[r] that effectively follow index r.

            Returns:
                Maximum points obtainable for the subproblem defined by (l, r, k).
            """
            # Base case: If the left index crosses the right index, the subarray is empty.
            if l > r:
                return 0

            # --- Optimization: Group consecutive boxes at the end ---
            # Find the actual start index (r_prime) of the rightmost block of boxes
            # with the same color as boxes[r].
            # Update the count k (to k_prime) to include these consecutive boxes
            # plus the original k boxes that were assumed to follow r.
            r_prime = r
            k_prime = k
            while r_prime > l and boxes[r_prime - 1] == boxes[r]:
                r_prime -= 1
                k_prime += 1
            # Now, boxes[r_prime...r] all have the same color (boxes[r]).
            # k_prime = original_k + (number of boxes in the block from r_prime to r-1)
            # The total number of same-colored boxes at the end is k_prime + 1 (the box at r_prime itself).

            # --- Option 1: Remove the rightmost block ---
            # Calculate the score by removing the block boxes[r_prime...r] along
            # with the k original following boxes.
            # The number of boxes removed is (r - r_prime + 1) + k = k_prime + 1.
            # The score for this move is (k_prime + 1) ** 2.
            # The remaining subproblem involves the subarray boxes[l...r_prime-1]
            # with 0 boxes following it.
            # Initialize the result with the score from this option.
            res = solve(l, r_prime - 1, 0) + (k_prime + 1) ** 2

            # --- Option 2: Merge with a previous box of the same color ---
            # Iterate through the subarray boxes[l...r_prime-1] to find a box boxes[i]
            # that has the same color as the rightmost block (boxes[r]).
            for i in range(l, r_prime):
                if boxes[i] == boxes[r]:
                    # If a matching box boxes[i] is found, consider removing the
                    # segment between boxes[i] and the rightmost block first.
                    # The score for removing the middle segment boxes[i+1...r_prime-1] is
                    # calculated by solve(i + 1, r_prime - 1, 0).
                    # After removing the middle part, boxes[i] becomes adjacent to the
                    # rightmost block (boxes[r_prime...r]) and the original k followers.
                    # The subproblem for the left part becomes solve(l, i, k_prime + 1),
                    # where k_prime + 1 represents the total count of boxes (the block
                    # plus original followers) that are now effectively following boxes[i].
                    current_score = solve(l, i, k_prime + 1) + solve(i + 1, r_prime - 1, 0)
                    # Update the result if this strategy yields a higher score.
                    res = max(res, current_score)

            # Return the maximum score found for the subproblem (l, r, k).
            return res

        # Start the calculation for the entire array boxes[0...n-1] with k=0 initially.
        return solve(0, n - 1, 0)

# Example Usage:
sol = Solution()
boxes1 = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print(f"Boxes: {boxes1}, Max Points: {sol.removeBoxes(boxes1)}") # Expected output: 23

boxes2 = [1, 1, 1]
print(f"Boxes: {boxes2}, Max Points: {sol.removeBoxes(boxes2)}") # Expected output: 9

boxes3 = [1]
print(f"Boxes: {boxes3}, Max Points: {sol.removeBoxes(boxes3)}") # Expected output: 1

boxes4 = [2, 2, 1, 2, 2]
print(f"Boxes: {boxes4}, Max Points: {sol.removeBoxes(boxes4)}") # Expected output: 17
