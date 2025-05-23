import math

class Solution:
  def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum possible sum of node values in a tree.
    The operation allows XORing values of connected nodes u and v with k.
    Any even number of nodes can be chosen to have their values XORed with k.
    """

    # dp_even: max sum with an even number of XOR operations on processed nodes.
    # dp_odd: max sum with an odd number of XOR operations on processed nodes.
    dp_even = 0
    # Initialize dp_odd to negative infinity as it's initially impossible
    # to have an odd number of XORs from zero processed elements.
    dp_odd = -float('inf') 

    for num_current_node in nums:
      val_if_not_xored = num_current_node
      val_if_xored = num_current_node ^ k # '^' is the XOR operator in Python

      # Store dp values from the *previous* iteration to use for current calculation
      prev_dp_even = dp_even
      prev_dp_odd = dp_odd

      # Calculate dp_even for the current element:
      # Option 1: Current node's value is NOT XORed.
      #   Requires an even number of XORs from previous elements.
      # Option 2: Current node's value IS XORed.
      #   Requires an odd number of XORs from previous elements.
      dp_even = max(prev_dp_even + val_if_not_xored, 
                    prev_dp_odd + val_if_xored)

      # Calculate dp_odd for the current element:
      # Option 1: Current node's value is NOT XORed.
      #   Requires an odd number of XORs from previous elements.
      # Option 2: Current node's value IS XORed.
      #   Requires an even number of XORs from previous elements.
      dp_odd = max(prev_dp_odd + val_if_not_xored,
                   prev_dp_even + val_if_xored)
            
    # The problem requires the final state to have an even number of total XOR operations.
    return dp_even
