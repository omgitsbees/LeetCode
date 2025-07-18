class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        import heapq
        
        n = len(nums) // 3
        
        # For each position i, we need to know:
        # 1. The sum of the smallest n elements from nums[0:i+1]
        # 2. The sum of the largest n elements from nums[i:3*n]
        
        # Calculate prefix_min: smallest n elements ending at each position
        prefix_min = [0] * (3 * n)
        min_heap = []
        current_sum = 0
        
        for i in range(3 * n):
            heapq.heappush(min_heap, -nums[i])  # Use negative for max heap
            current_sum += nums[i]
            
            if len(min_heap) > n:
                # Remove the largest element (smallest negative)
                removed = -heapq.heappop(min_heap)
                current_sum -= removed
            
            if len(min_heap) == n:
                prefix_min[i] = current_sum
        
        # Calculate suffix_max: largest n elements starting from each position
        suffix_max = [0] * (3 * n)
        max_heap = []
        current_sum = 0
        
        for i in range(3 * n - 1, -1, -1):
            heapq.heappush(max_heap, nums[i])  # Min heap for smallest elements
            current_sum += nums[i]
            
            if len(max_heap) > n:
                # Remove the smallest element
                removed = heapq.heappop(max_heap)
                current_sum -= removed
            
            if len(max_heap) == n:
                suffix_max[i] = current_sum
        
        # Find minimum difference
        min_diff = float('inf')
        
        # Try all valid split points
        # We need at least n elements before and after the split
        for i in range(n - 1, 2 * n):
            sumfirst = prefix_min[i]
            sumsecond = suffix_max[i + 1]
            min_diff = min(min_diff, sumfirst - sumsecond)
        
        return min_diff
