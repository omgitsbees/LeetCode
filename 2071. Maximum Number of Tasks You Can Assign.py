# Requires: pip install sortedcontainers
from sortedcontainers import SortedList
from typing import List

class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        # Check function using the logic from the provided SortedList solution
        def check(k: int) -> bool:
            """Checks if the k easiest tasks can be assigned using the k strongest workers."""
            if k == 0:
                return True
            # Need at least k workers from the strongest pool
            if k > m:
                return False

            p = pills
            # Use only the k strongest workers
            ws = SortedList(workers[m - k :]) # O(k log k) construction

            # Iterate through the k easiest tasks, from hardest (k-1) to easiest (0)
            for i in range(k - 1, -1, -1):
                current_task_strength = tasks[i]

                # Check if the strongest available worker can do the task without a pill
                # ws[-1] gives the maximum element in O(log k)
                if ws[-1] >= current_task_strength:
                    # Yes, assign the strongest available worker (greedy choice 1)
                    ws.pop() # Removes the maximum element in O(log k)
                else:
                    # No, need to use a pill
                    if p == 0: # No pills left
                        return False

                    # Find the weakest worker who can do the task WITH a pill
                    # Need worker strength w >= current_task_strength - strength
                    threshold = current_task_strength - strength
                    # Find index of first worker >= threshold in O(log k)
                    idx = ws.bisect_left(threshold)

                    if idx == len(ws):
                        # No worker is strong enough even with a pill
                        return False

                    # Assign the weakest suitable worker (greedy choice 2) and use a pill
                    p -= 1
                    # Remove element at index idx in O(log k)
                    ws.pop(idx)

            # All k tasks were assigned
            return True

        # Binary search for the maximum k
        # Range is 0 to min(m, n) inclusive
        left, right, ans = 0, min(m, n), 0
        while left <= right:
            mid = left + (right - left) // 2 # Midpoint calculation
            if check(mid):
                ans = mid # Found a possible solution, try for more
                left = mid + 1
            else:
                right = mid - 1 # Too many tasks, try fewer

        return ans
