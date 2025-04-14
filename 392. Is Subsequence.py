class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for string s
        s_pointer = 0
        
        # Iterate through each character in t
        for char in t:
            # If the current character matches the current character in s
            if s_pointer < len(s) and char == s[s_pointer]:
                s_pointer += 1
                
        # If we have gone through all characters of s, it is a subsequence
        return s_pointer == len(s)
