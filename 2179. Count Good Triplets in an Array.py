from typing import List

class FenwickTree:
    """Fenwick Tree for efficient range queries and updates"""
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index
        return sum_val

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Step 1: Compute positions for each element
        pos1 = {num: i for i, num in enumerate(nums1)}
        pos2 = {num: i for i, num in enumerate(nums2)}

        # Step 2: Fenwick Tree to count valid pairs (x, y)
        fenwick1 = FenwickTree(n)
        pair_count = [0] * n  # Track valid (x, y) pairs dynamically

        # Step 3: Fenwick Tree to count good triplets (x, y, z)
        fenwick2 = FenwickTree(n)
        result = 0

        for num in nums1:
            idx2 = pos2[num]

            # Count valid (x, y) where pos1x < pos1y and pos2x < pos2y
            left_pairs = fenwick1.query(idx2)
            pair_count[idx2] += left_pairs
            fenwick1.update(idx2 + 1, 1)

            # Count valid triplets where pos1x < pos1y < pos1z and pos2x < pos2y < pos2z
            triplet_count = fenwick2.query(idx2)
            result += triplet_count
            fenwick2.update(idx2 + 1, pair_count[idx2])

        return result
