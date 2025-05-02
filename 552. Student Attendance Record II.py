import sys

# Increase recursion depth limit for potential recursive solutions (though DP is better here)
# sys.setrecursionlimit(2000) # Usually not needed for iterative DP

class Solution:
    def checkRecord(self, n: int) -> int:
        """
        Calculates the number of possible attendance records of length n
        that are eligible for an award, modulo 10^9 + 7.

        Eligibility criteria:
        1. Fewer than 2 total absences ('A').
        2. No 3 or more consecutive lates ('L').

        Args:
            n: The length of the attendance record.

        Returns:
            The number of valid attendance records modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # DP state: dp[i][a][l]
        # i: length of the record considered so far (implicitly tracked by the loop)
        # a: total number of absences ('A') used so far (0 or 1)
        # l: number of consecutive lates ('L') at the end of the record (0, 1, or 2)

        # We only need the previous day's state to calculate the current day's state.
        # So, we can optimize space using only two layers (prev_dp and current_dp).
        # Initialize dp for length 0 (empty string)
        # dp[a][l]
        prev_dp = [[0] * 3 for _ in range(2)]
        prev_dp[0][0] = 1  # Empty string: 0 Absences, 0 trailing Lates

        for _ in range(n): # Iterate from length 1 to n
            current_dp = [[0] * 3 for _ in range(2)]

            # Calculate current_dp based on prev_dp

            # Case 1: Add 'P' (Present)
            # Appending 'P' doesn't change the absence count 'a'.
            # Appending 'P' resets the consecutive late count 'l' to 0.
            # It can be added to any valid previous state.
            for a in range(2):
                for l in range(3):
                    current_dp[a][0] = (current_dp[a][0] + prev_dp[a][l]) % MOD

            # Case 2: Add 'A' (Absent)
            # Appending 'A' is only possible if the previous absence count 'a' was 0.
            # The new absence count becomes 1.
            # Appending 'A' resets the consecutive late count 'l' to 0.
            # It can be added to any valid previous state with a=0.
            for l in range(3):
                 current_dp[1][0] = (current_dp[1][0] + prev_dp[0][l]) % MOD

            # Case 3: Add 'L' (Late)
            # Appending 'L' doesn't change the absence count 'a'.
            # Appending 'L' increments the consecutive late count 'l'.
            # This is only possible if the previous late count 'l' was less than 2.
            for a in range(2):
                # If prev state ended with 0 Lates (l=0), adding 'L' makes it end with 1 Late (l=1)
                current_dp[a][1] = (current_dp[a][1] + prev_dp[a][0]) % MOD
                # If prev state ended with 1 Late (l=1), adding 'L' makes it end with 2 Lates (l=2)
                current_dp[a][2] = (current_dp[a][2] + prev_dp[a][1]) % MOD
                # Cannot transition from l=2 by adding 'L' as it would violate the constraint.

            # Update prev_dp for the next iteration
            prev_dp = current_dp

        # The final answer is the sum of all valid states for length n
        total_valid_records = 0
        for a in range(2):
            for l in range(3):
                total_valid_records = (total_valid_records + prev_dp[a][l]) % MOD

        return total_valid_records
