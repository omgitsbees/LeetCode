class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        pref_t = [0 for _ in range(n)]
        pref_t[0] = time[0]

        for i in range(1, n):
            pref_t[i] = pref_t[i - 1] + time[i]

        dp = [[dict() for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][time[0]] = 0

        for i in range(n):
            for m in range(k + 1):
                for accum, time_t in list(dp[i][m].items()):
                    for j in range(i + 1, n):
                        rem = j - i - 1
                        if m + rem > k:
                            continue
                        seg_time = (position[j] - position[i]) * accum
                        new_time = time_t + seg_time
                        new_acc = pref_t[j] - pref_t[i]
                        rd = m + rem
                        curr = dp[j][rd].get(new_acc)
                        if curr is None or new_time < curr:
                            dp[j][rd][new_acc] = new_time

        res = float("inf")
        for time_t in dp[n - 1][k].values():
            res = min(res, time_t)
        return res
