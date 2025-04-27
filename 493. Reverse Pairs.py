from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # Temporary array used during the merge process
        temp = [0] * n 

        def merge_sort_and_count(low, high):
            # Base case: subarray of size 0 or 1 has no pairs
            if low >= high:
                return 0

            mid = (low + high) // 2

            # 1. Recursively count pairs in the left half
            count = merge_sort_and_count(low, mid)
            # 2. Recursively count pairs in the right half
            count += merge_sort_and_count(mid + 1, high)

            # 3. Count pairs where i is in left half, j is in right half
            # nums[i] > 2 * nums[j]
            # Both nums[low...mid] and nums[mid+1...high] are sorted now
            
            j = mid + 1 # Pointer for the right half
            for i in range(low, mid + 1): # Pointer for the left half
                # Move j forward while the condition holds
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                # Add the number of valid j's found for this i
                # (all elements from mid+1 up to j-1 satisfy the condition)
                count += (j - (mid + 1)) 

            # 4. Merge the two sorted halves [low...mid] and [mid+1...high]
            # --- Standard Merge Logic ---
            p1, p2 = low, mid + 1
            k = low # Write pointer for the temp array
            
            # Merge into the temporary array
            while p1 <= mid and p2 <= high:
                if nums[p1] <= nums[p2]:
                    temp[k] = nums[p1]
                    p1 += 1
                else:
                    temp[k] = nums[p2]
                    p2 += 1
                k += 1
            
            # Copy any remaining elements from the left half
            while p1 <= mid:
                temp[k] = nums[p1]
                p1 += 1
                k += 1
                
            # Copy any remaining elements from the right half
            while p2 <= high:
                temp[k] = nums[p2]
                p2 += 1
                k += 1

            # Copy the sorted merged result from temp back to the original nums array
            # This ensures the array segment is sorted for higher levels of recursion
            nums[low:high+1] = temp[low:high+1]
            # --- End Merge Logic ---

            return count

        # Start the recursive process on the entire array
        return merge_sort_and_count(0, n - 1)
