import collections
from typing import List

class Solution:
  def longestPalindrome(self, words: List[str]) -> int:
    length = 0
    # This flag will be true if there is at least one palindromic word 
    # (e.g., "gg", "aa") with an odd count, allowing it to be a potential center.
    can_add_center_from_palindromic_word = False
    
    counts = collections.Counter(words)

    for word, count_of_this_word in counts.items():
      # Case 1: The word is a palindrome itself (e.g., "gg", "aa")
      if word[0] == word[1]:
        # Add pairs of this word (e.g., "gg...gg")
        # Each word is length 2. A pair like "gg" on one side and "gg" on the other contributes 2*2 = 4 to length.
        length += (count_of_this_word // 2) * 4 
        
        # If there's an odd one out after forming pairs, it can be a candidate for the center
        if count_of_this_word % 2 == 1:
          can_add_center_from_palindromic_word = True # Mark that *a* center is possible
      
      # Case 2: The word is not a palindrome itself (e.g., "lc")
      else:
        # To avoid double counting pairs like ("lc", "cl"), we only process 
        # when `word` is lexicographically smaller than its `reverse_word`.
        # For example, if `word` is "cl", `reverse_word` is "lc". "cl" < "lc" is true, so process.
        # If `word` is "lc", `reverse_word` is "cl". "lc" < "cl" is false, so skip "lc"
        # because "cl" (which is smaller) would have handled this pair if it exists.
        reverse_word = word[1] + word[0]
        if word < reverse_word: 
          if reverse_word in counts:
            # Number of pairs like "word...reverse_word" we can form.
            # This is limited by the minimum count of `word` and `reverse_word`.
            num_pairs = min(count_of_this_word, counts[reverse_word])
            # Each such pair adds 4 to the total length (e.g., "lc" at start, "cl" at end).
            length += num_pairs * 4
            
    # If we found any palindromic word with an odd count that could form a center
    # (e.g., "gg" appearing 3 times, where two "gg"s form a pair and one "gg" is left over),
    # we can add this single leftover word (length 2) to the center of the palindrome.
    # Only one such word can be the center.
    if can_add_center_from_palindromic_word:
      length += 2
      
    return length
