class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Dictionary to store sum of digits and their occurrences
        digit_sum_groups = {}
        
        # Calculate sum of digits for each number from 1 to n
        for i in range(1, n + 1):
            digit_sum = sum(map(int, str(i)))  # Sum of digits of the number
            if digit_sum in digit_sum_groups:
                digit_sum_groups[digit_sum] += 1
            else:
                digit_sum_groups[digit_sum] = 1
        
        # Find the maximum size among all groups
        max_size = max(digit_sum_groups.values())
        
        # Count the number of groups with the maximum size
        largest_groups_count = sum(1 for size in digit_sum_groups.values() if size == max_size)
        
        return largest_groups_count
