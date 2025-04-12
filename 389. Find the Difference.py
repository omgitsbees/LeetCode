class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a variable to store the XOR result
        xor_result = 0
        
        # XOR all characters in string s
        for char in s:
            xor_result ^= ord(char)
        
        # XOR all characters in string t
        for char in t:
            xor_result ^= ord(char)
        
        # The result will be the ASCII value of the added character
        return chr(xor_result)

# Example usage:
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))          # Output: "y"
