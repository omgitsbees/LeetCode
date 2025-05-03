import math

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        Finds the closest palindrome to the given integer string n.

        Args:
          n: A string representing an integer.

        Returns:
          A string representing the closest palindrome integer. If there's a tie,
          the smaller palindrome is returned.
        """
        l = len(n)
        num_n = int(n)
        candidates = set()

        # 1. Candidates based on the prefix of n
        prefix_val = int(n[:(l + 1) // 2])

        for p_val in [prefix_val - 1, prefix_val, prefix_val + 1]:
            if p_val < 0:  # Avoid negative prefixes if prefix_val was 0
                continue
            s = str(p_val)
            if l % 2 == 0:
                # Even length: prefix + reversed(prefix)
                candidate_str = s + s[::-1]
            else:
                # Odd length: prefix + reversed(prefix without last char)
                candidate_str = s + s[:-1][::-1]

            # Avoid leading zeros unless it's just "0"
            if len(candidate_str) > 1 and candidate_str.startswith('0'):
                 continue
            if not candidate_str: # Handle empty string if p_val becomes 0 for l=1
                 candidate_str = "0"

            candidates.add(int(candidate_str))


        # 2. Edge case candidates: Palindromes with l-1 and l+1 digits
        # Smallest palindrome with l+1 digits (10...01)
        candidates.add(10**l + 1)
        # Largest palindrome with l-1 digits (9...9). Handle l=1 case where it's 0.
        if l > 1:
             candidates.add(10**(l - 1) - 1)
        else:
             candidates.add(0) # For n="1", 10**(1-1)-1 = 0

        # 3. Remove n itself from candidates
        candidates.discard(num_n)

        # 4. Find the closest candidate
        min_diff = float('inf')
        result = -1 # Initialize result

        # Sort candidates to handle ties correctly (prefer smaller number)
        sorted_candidates = sorted(list(candidates))

        for cand_val in sorted_candidates:
            diff = abs(cand_val - num_n)

            if diff < min_diff:
                min_diff = diff
                result = cand_val
            # Since candidates are sorted, the first one encountered
            # with the minimum difference will be the smaller one in case of a tie.

        return str(result)
