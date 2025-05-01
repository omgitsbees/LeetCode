from typing import List

class Solution:
    """
    Solves the LeetCode problem "Average Waiting Time".
    Calculates the average time customers wait for their orders in a restaurant
    with a single chef processing orders sequentially.
    """
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Calculates the average waiting time for all customers.

        Args:
            customers: A list where each element is [arrival_i, time_i],
                       representing the arrival time and order preparation time
                       for the i-th customer. Arrival times are sorted.

        Returns:
            The average waiting time as a float.
        """
        n = len(customers)
        # If there are no customers, the average waiting time is 0.
        if n == 0:
            return 0.0

        total_waiting_time = 0
        # Tracks the time when the chef becomes free after finishing the current order.
        # Initialize to 0, assuming the chef starts idle at time 0 or before the first customer.
        chef_free_time = 0

        # Simulate the process for each customer in the order they arrive.
        for i in range(n):
            arrival_i = customers[i][0]
            time_i = customers[i][1] # Time needed to prepare the order

            # Determine when the chef can start preparing the current order.
            # The chef cannot start before the customer arrives (arrival_i) and
            # cannot start before finishing the previous order (chef_free_time).
            start_time_i = max(arrival_i, chef_free_time)

            # Determine when the chef finishes the current order.
            finish_time_i = start_time_i + time_i

            # Calculate the waiting time for the current customer.
            # Waiting time = (Time order finished) - (Time customer arrived)
            wait_time_i = finish_time_i - arrival_i

            # Add the current customer's waiting time to the total.
            total_waiting_time += wait_time_i

            # Update the time when the chef will be free for the next customer.
            chef_free_time = finish_time_i

        # Calculate the average waiting time by dividing the total waiting time
        # by the number of customers. Python 3 division automatically yields a float.
        average_waiting_time = total_waiting_time / n

        return average_waiting_time
