import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log(n, 2))  # Maximum possible value for m
        
        for m in range(max_m, 1, -1):
            k = int(n ** (1 / m))  # Potential base
            if (k**(m+1) - 1) // (k - 1) == n:
                return str(k)
        
        return str(n - 1)  # If no smaller base is found, n - 1 is the smallest good base
