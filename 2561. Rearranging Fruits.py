from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Count frequency of each fruit in both baskets
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        # Get all unique fruits
        all_fruits = set(basket1) | set(basket2)
        
        # Check if it's possible to make baskets equal
        # Each fruit type must appear even number of times total
        for fruit in all_fruits:
            total_count = count1.get(fruit, 0) + count2.get(fruit, 0)
            if total_count % 2 != 0:
                return -1
        
        # Find fruits that need to be moved from basket1 to basket2
        # and vice versa
        excess_in_basket1 = []  # fruits that basket1 has too many of
        excess_in_basket2 = []  # fruits that basket2 has too many of
        
        for fruit in all_fruits:
            count_in_1 = count1.get(fruit, 0)
            count_in_2 = count2.get(fruit, 0)
            target_count = (count_in_1 + count_in_2) // 2
            
            if count_in_1 > target_count:
                # basket1 has excess of this fruit
                excess = count_in_1 - target_count
                excess_in_basket1.extend([fruit] * excess)
            elif count_in_2 > target_count:
                # basket2 has excess of this fruit
                excess = count_in_2 - target_count
                excess_in_basket2.extend([fruit] * excess)
        
        # Sort excess_in_basket1 in ascending order and excess_in_basket2 in descending order
        # This way we pair cheap fruits from basket1 with expensive fruits from basket2
        excess_in_basket1.sort()
        excess_in_basket2.sort(reverse=True)
        
        # Find the minimum element across both baskets for potential indirect swaps
        min_element = min(min(basket1), min(basket2))
        
        total_cost = 0
        n = len(excess_in_basket1)
        
        # Process swaps optimally
        for i in range(n):
            fruit1 = excess_in_basket1[i]  # from basket1 (sorted ascending)
            fruit2 = excess_in_basket2[i]  # from basket2 (sorted descending)
            
            # Cost of direct swap
            direct_cost = min(fruit1, fruit2)
            
            # Cost of indirect swap using minimum element as intermediary
            # We swap fruit1 with min_element (cost = min(fruit1, min_element) = min_element)
            # Then swap min_element with fruit2 (cost = min(min_element, fruit2) = min_element)
            # Total cost = 2 * min_element
            indirect_cost = 2 * min_element
            
            # Choose the cheaper option
            total_cost += min(direct_cost, indirect_cost)
        
        return total_cost

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    basket1 = [4, 2, 2, 2]
    basket2 = [1, 4, 1, 2]
    print(f"Test 1: {sol.minCost(basket1, basket2)}")  # Expected: 1
    
    # Test case 2  
    basket1 = [2, 3, 4, 1]
    basket2 = [3, 2, 5, 1]
    print(f"Test 2: {sol.minCost(basket1, basket2)}")  # Expected: 1
    
    # Test case 3 - impossible case
    basket1 = [1, 2]
    basket2 = [3, 4]
    print(f"Test 3: {sol.minCost(basket1, basket2)}")  # Expected: -1

if __name__ == "__main__":
    test_solution()
