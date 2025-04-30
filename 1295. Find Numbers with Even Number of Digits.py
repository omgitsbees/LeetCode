import math
from typing import List

class Solution:
    """
    This class provides solutions to find the count of numbers
    in a list that have an even number of digits.
    """
    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts the numbers in the input list with an even number of digits
        by converting each number to a string and checking its length.

        Args:
            nums: A list of integers. The constraints are:
                  1 <= nums.length <= 500
                  1 <= nums[i] <= 10^5

        Returns:
            The count of numbers in nums that have an even number of digits.
        """
        even_digit_count = 0  # Initialize counter for numbers with even digits

        for num in nums:
            # Convert the number to a string to easily find its length (number of digits)
            num_str = str(num)
            number_of_digits = len(num_str)

            # Check if the number of digits is even using the modulo operator
            if number_of_digits % 2 == 0:
                even_digit_count += 1 # Increment counter if the digit count is even

        return even_digit_count

    # --- Alternative Solutions ---

    def findNumbers_comprehension(self, nums: List[int]) -> int:
        """
        Counts the numbers with an even number of digits using a more concise
        list comprehension or generator expression approach.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers in nums that have an even number of digits.
        """
        # sum() will add 1 for each True condition (len(str(num)) % 2 == 0)
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

    def findNumbers_log(self, nums: List[int]) -> int:
        """
        Counts the numbers with an even number of digits using logarithms
        to determine the number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers in nums that have an even number of digits.
        """
        even_digit_count = 0
        for num in nums:
            # The number of digits in a positive integer 'n' is floor(log10(n)) + 1.
            # Constraint nums[i] >= 1 ensures num is positive, so log10 is defined.
            number_of_digits = math.floor(math.log10(num)) + 1

            if number_of_digits % 2 == 0:
                even_digit_count += 1

        return even_digit_count
