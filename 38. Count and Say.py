class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        seq = "1"
        for _ in range(n - 1):
            new_seq = ""
            i = 0
            while i < len(seq):
                count = 1
                while i + 1 < len(seq) and seq[i] == seq[i + 1]:
                    i += 1
                    count += 1
                new_seq += str(count) + seq[i]
                i += 1
            seq = new_seq

        return seq
