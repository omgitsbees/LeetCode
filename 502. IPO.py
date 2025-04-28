import heapq
from typing import List

class Solution:
    """
    Solves the LeetCode problem "IPO" (Maximize Capital).

    The problem involves selecting at most k projects to maximize final capital,
    given initial capital w, project profits, and project capital requirements.
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Calculates the maximum capital achievable by completing at most k projects.

        Args:
            k: The maximum number of distinct projects that can be finished.
            w: The initial capital.
            profits: A list where profits[i] is the profit of the ith project.
            capital: A list where capital[i] is the minimum capital needed to start the ith project.

        Returns:
            The final maximized capital after finishing at most k projects.
        """
        n = len(profits)

        # 1. Create a list of projects combining capital requirements and profits.
        #    Store as tuples: (capital_required, profit)
        projects = list(zip(capital, profits))

        # 2. Sort the projects based on their capital requirement in ascending order.
        #    This allows us to efficiently find projects we can afford as our capital increases.
        projects.sort()  # O(N log N)

        # 3. Use a Max Heap (implemented as a Min Heap storing negative profits)
        #    to keep track of the profits of all projects currently affordable.
        #    This allows us to quickly select the most profitable affordable project.
        affordable_profits_heap = []
        
        project_index = 0  # Pointer to the next project in the sorted list to consider
        current_capital = w

        # 4. Iterate up to k times, selecting one project in each iteration.
        for _ in range(k):
            # 5. Add all newly affordable projects to the max-heap.
            #    These are projects whose capital requirement is less than or equal to
            #    our current capital. We check projects from the current project_index onwards.
            while project_index < n and projects[project_index][0] <= current_capital:
                # Push the negative profit onto the min-heap.
                heapq.heappush(affordable_profits_heap, -projects[project_index][1]) # O(log N) or O(log P) where P is heap size <= N
                project_index += 1
            
            # 6. If the heap is empty, it means there are no affordable projects
            #    left that we can undertake with our current capital. Stop early.
            if not affordable_profits_heap:
                break
                
            # 7. Greedily select the most profitable project among the affordable ones.
            #    This corresponds to the smallest element (most negative) in the min-heap.
            #    Pop it and negate it back to get the actual maximum profit.
            max_profit = -heapq.heappop(affordable_profits_heap) # O(log N) or O(log P)
            
            # 8. Add the chosen project's profit to our current capital.
            current_capital += max_profit
            
        # 9. Return the final maximized capital after k iterations or stopping early.
        return current_capital
