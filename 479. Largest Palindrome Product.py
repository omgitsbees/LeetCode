class Solution:
    def largestPalindrome(self, n: int):
        if n == 1: return 9
        for i in range(1, 99999999):
            left = str(10**n - 2*i)
            right = left[::-1]
            if i**2 > int(right) \
            and sqrt(i**2 - int(right)).is_integer():
                return int(left + right) % 1337
