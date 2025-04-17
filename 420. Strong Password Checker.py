class Solution(object):
    def strongPasswordChecker(self, s):
        # edge case where s size is 0
        if len(s) == 0:
            return 6
        # edge case where s size is 1
        if len(s) == 1:
            return 5
        
        cnt = 0  # no. of changes needed for consecutive characters
        mpp = {"uppercase": 0, "lowercase": 0, "digits": 0}
        i = 0

        # We use a hashmap to check the number of 1.) Uppercases' 2.) Lowercases' 3.) Numbers
        while i < len(s):
            if s[i].isupper(): mpp["uppercase"] += 1
            elif s[i].islower(): mpp["lowercase"] += 1
            elif s[i].isdigit(): mpp["digits"] += 1

            # checking if there are 3 consecutive characters
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            length = j - i
            if length >= 3:
                cnt += length // 3
            i = j

        cnt1 = 0  # To check if one of the alphanumeric's is not present in the password
        if mpp["uppercase"] == 0: cnt1 += 1
        if mpp["lowercase"] == 0: cnt1 += 1
        if mpp["digits"] == 0: cnt1 += 1

        # If the password size is less than 6, return the number of characters needed to reach size 6
        if len(s) < 6:
            return max(6 - len(s), cnt1)
        elif len(s) > 20:
            length = len(s) - 20
            res = [0] * 3  # No. of reductions needed when 3 consecutive characters are present in a series
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[i] == s[j]:
                    j += 1
                lenConsec = j - i
                if lenConsec >= 3:
                    res[lenConsec % 3] += 1
                i = j

            for k in range(3):
                if length <= 0:
                    break
                mini = min(res[k], length // (k + 1))
                cnt -= mini
                length -= mini * (k + 1)

            cnt -= length // 3
            return (len(s) - 20) + max(cnt, cnt1)

        # If the size is within limits, return maximum of missing types or required consecutive fixes
        return max(cnt, cnt1)
