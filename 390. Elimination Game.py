class Solution:
    def lastRemaining(self, n: int) -> int:
        # Initialize variables
        head = 1  # Starting element
        step = 1  # Initial step size
        left_to_right = True  # Start elimination from left to right
        remaining = n  # Number of elements remaining

        # Loop until only one element remains
        while remaining > 1:
            # Update the head based on the direction and remaining count
            if left_to_right or remaining % 2 == 1:
                head += step
            
            # Double the step size for the next round
            step *= 2
            # Toggle the direction
            left_to_right = not left_to_right
            # Halve the remaining count
            remaining //= 2

        return head
