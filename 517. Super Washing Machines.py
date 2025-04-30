import math
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        Calculates the minimum number of moves to equalize dresses in washing machines.

        Args:
            machines: A list of integers representing dresses in each machine.

        Returns:
            The minimum number of moves, or -1 if impossible.
        """
        n = len(machines)
        if n == 0:
            return 0 # Or handle as an edge case if constraints guarantee n >= 1

        total_dresses = sum(machines)

        # Check if equalization is possible
        if total_dresses % n != 0:
            return -1

        target = total_dresses // n
        max_moves = 0
        current_balance = 0  # Tracks the net flow requirement across boundaries (sum of balances so far)

        for dresses in machines:
            # Calculate how many dresses this machine needs to give away (+) or receive (-)
            # This is also the max moves this single machine *must* initiate if positive.
            machine_balance = dresses - target

            # Update the running balance. current_balance represents the net number
            # of dresses that need to cross the boundary to the right of the current machine.
            # A positive value means net flow right is needed.
            # A negative value means net flow left is needed.
            # abs(current_balance) is the minimum moves required to achieve this flow.
            current_balance += machine_balance

            # The overall minimum moves is the maximum of:
            # 1. The max dresses any single machine needs to give out (machine_balance if > 0).
            # 2. The max net flow required across any boundary (abs(current_balance)).
            max_moves = max(max_moves, abs(current_balance), machine_balance)

        return max_moves
