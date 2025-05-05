class Solution:
    def numTilings(self, n: int) -> int:
        """
        Calculates the number of ways to tile a 2xn board using 2x1 dominoes
        and L-shaped trominoes (rotatable), modulo 10^9 + 7.

        Args:
            n: The width of the board.

        Returns:
            The number of tiling ways modulo 10^9 + 7.
        """
        MOD = 1_000_000_007

        # Base cases for small n
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        # dp[i] stores the number of ways to tile a 2xi board
        dp = [0] * (n + 1)

        # Initialize base cases in dp array
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        # Calculate dp values using the recurrence relation:
        # dp[i] = 2 * dp[i-1] + dp[i-3]
        # This relation comes from considering the ways to finish tiling the i-th column:
        # 1. Add a vertical domino to a fully tiled 2x(i-1) board: dp[i-1] ways.
        # 2. Add two horizontal dominoes to a fully tiled 2x(i-2) board: dp[i-2] ways.
        # 3. Add a tromino covering (i-1, 0), (i, 0), (i, 1) to a board with (i-1, 1) uncovered: dp_partial_bottom[i-1] ways.
        # 4. Add a tromino covering (i-1, 1), (i, 0), (i, 1) to a board with (i-1, 0) uncovered: dp_partial_top[i-1] ways.
        # Combining these leads to the simpler recurrence dp[i] = 2 * dp[i-1] + dp[i-3] after some derivations.
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
