class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Helper function for fast exponentiation
        def power(x, y, p):
            res = 1
            x = x % p
            while y > 0:
                # If y is odd, multiply x with result
                if y % 2 == 1:
                    res = (res * x) % p
                # Divide y by 2 and square x
                y //= 2
                x = (x * x) % p
            return res
        
        # Calculate the number of even and odd indices
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        # Calculate powers
        even_digits = power(5, even_count, MOD)
        odd_digits = power(4, odd_count, MOD)
        
        # Return result
        return (even_digits * odd_digits) % MOD
