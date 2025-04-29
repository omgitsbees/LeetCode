import math

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        # Precompute indices for each character for quick lookup
        # char_indices['c'] = [list of indices where 'c' appears in ring]
        char_indices = {}
        for i, char in enumerate(ring):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        # dp[i][j]: min steps to spell key[i:] starting with ring[j] at 12:00
        # Initialize with infinity, as we are looking for the minimum
        # Dimensions: (m + 1) for key indices (0 to m)
        #             n for ring positions (0 to n-1)
        dp = [[math.inf] * n for _ in range(m + 1)]

        # Base case: Spelling an empty key suffix takes 0 steps
        for j in range(n):
            dp[m][j] = 0

        # Fill the DP table bottom-up (from i = m-1 down to 0)
        for i in range(m - 1, -1, -1):
            target_char = key[i]
            # Iterate through all possible previous ring positions (j)
            # This 'j' represents the ring position *before* spelling key[i]
            for j in range(n):
                min_steps_for_this_state = math.inf
                # Consider all possible ring indices 'k' where the target character exists
                for k in char_indices[target_char]:
                    # Calculate minimum rotation steps from j to k
                    diff = abs(j - k)
                    rotate_steps = min(diff, n - diff)

                    # Press cost is always 1
                    press_steps = 1

                    # Get the cost from the next state (already computed)
                    # Cost to spell key[i+1:] starting from position k
                    recursive_cost = dp[i+1][k]

                    # Calculate total cost for this path (rotate j->k, press, continue)
                    total_cost = rotate_steps + press_steps + recursive_cost

                    # Update the minimum steps needed to reach state (i, j)
                    min_steps_for_this_state = min(min_steps_for_this_state, total_cost)

                # Store the calculated minimum steps for state dp[i][j]
                dp[i][j] = min_steps_for_this_state

        # The final answer is the minimum cost to spell the entire key (key[0:]),
        # starting with ring[0] at the 12:00 position.
        return dp[0][0]
