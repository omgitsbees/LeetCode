import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Initialize an array to hold the current window and the result
        window = sorted(nums[:k])
        medians = []
        
        for i in range(k, len(nums) + 1):
            # Calculate the median of the current window
            if k % 2 == 0:
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2)
            else:
                medians.append(window[k // 2])
            
            if i < len(nums):
                # Remove the element sliding out of the window
                window.remove(nums[i - k])
                # Insert the next element sliding into the window
                bisect.insort(window, nums[i])
        
        return medians
