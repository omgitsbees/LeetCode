class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i][j] represents the number of distinct palindromic subsequences in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1
        
        # Fill for all substring lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # Find the next occurrence of s[i] after position i
                    left = i + 1
                    while left <= j - 1 and s[left] != s[i]:
                        left += 1
                    
                    # Find the previous occurrence of s[i] before position j
                    right = j - 1
                    while right >= i + 1 and s[right] != s[i]:
                        right -= 1
                    
                    if left > right:
                        # No same character in the middle
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD
                    elif left == right:
                        # Exactly one same character in the middle
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD
                    else:
                        # Multiple same characters in the middle
                        dp[i][j] = (2 * dp[i + 1][j - 1] - dp[left + 1][right - 1] + MOD) % MOD
                else:
                    # Characters at both ends are different
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + MOD) % MOD
        
        return dp[0][n - 1]


# Test the solution
def test_solution():
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("bccb", 6),
        ("a", 1),
        ("aa", 2),
        ("aab", 4),
        ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", None)
    ]
    
    for s, expected in test_cases:
        result = sol.countPalindromicSubsequences(s)
        if expected:
            print(f"Input: '{s}' -> Output: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        else:
            print(f"Input: '{s}' -> Output: {result}")
    
    # Let's trace through "bccb" manually
    print("\nTracing 'bccb':")
    s = "bccb"
    print("Palindromic subsequences should be:")
    print("Single chars: 'b' (appears twice but distinct), 'c' (appears twice but distinct)")
    print("Two chars: 'bb', 'cc'") 
    print("Three chars: 'bcb'")
    print("Four chars: 'bccb'")
    print("Total distinct: b, c, bb, cc, bcb, bccb = 6")

if __name__ == "__main__":
    test_solution()
