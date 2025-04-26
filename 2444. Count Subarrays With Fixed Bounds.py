class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_index = -1  # Last index where nums[i] == minK
        max_index = -1  # Last index where nums[i] == maxK
        start_index = -1  # Start of the valid window
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                start_index = i  # Reset the window if the number is invalid
            
            if num == minK:
                min_index = i  # Update the last position of minK
            
            if num == maxK:
                max_index = i  # Update the last position of maxK
            
            # The number of fixed-bound subarrays ending at index i
            count += max(0, min(min_index, max_index) - start_index)
        
        return count
