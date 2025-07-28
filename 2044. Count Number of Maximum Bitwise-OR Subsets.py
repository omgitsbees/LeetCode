from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Find the maximum possible OR (OR of all elements)
        max_or = 0
        for num in nums:
            max_or |= num
        
        count = 0
        n = len(nums)
        
        # Check all non-empty subsets using bit manipulation
        # Iterate from 1 to 2^n - 1 (all non-empty subsets)
        for mask in range(1, 1 << n):
            current_or = 0
            
            # Calculate OR for current subset
            for i in range(n):
                if mask & (1 << i):  # If i-th bit is set
                    current_or |= nums[i]
            
            # If this subset achieves maximum OR, increment count
            if current_or == max_or:
                count += 1
        
        return count

# Alternative recursive solution with memoization
class SolutionRecursive:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Find maximum possible OR
        max_or = 0
        for num in nums:
            max_or |= num
        
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            
            # Choice 1: Don't include current element
            count = backtrack(index + 1, current_or)
            
            # Choice 2: Include current element
            count += backtrack(index + 1, current_or | nums[index])
            
            return count
        
        return backtrack(0, 0)

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: [3, 1]
    # Max OR = 3|1 = 3
    # Subsets: [3] -> 3, [1] -> 1, [3,1] -> 3
    # Count with max OR: 2
    assert sol.countMaxOrSubsets([3, 1]) == 2
    
    # Test case 2: [2, 2, 2]
    # Max OR = 2|2|2 = 2
    # All subsets have OR = 2
    # Non-empty subsets: 2^3 - 1 = 7
    assert sol.countMaxOrSubsets([2, 2, 2]) == 7
    
    # Test case 3: [3, 2, 1, 5]
    # Max OR = 3|2|1|5 = 7
    # Need to count subsets with OR = 7
    result = sol.countMaxOrSubsets([3, 2, 1, 5])
    print(f"Test case [3, 2, 1, 5]: {result}")
    
    print("All basic tests passed!")

if __name__ == "__main__":
    test_solution()
