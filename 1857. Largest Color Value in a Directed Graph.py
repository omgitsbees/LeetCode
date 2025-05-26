from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        # dp[u][c] = max count of color c in a path ending at u
        dp = [[0] * 26 for _ in range(n)]
        
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                # Base case: path of length 1 ending at node i
                dp[i][ord(colors[i]) - ord('a')] = 1
        
        processed_nodes_count = 0
        max_color_value = 0

        while q:
            u = q.popleft()
            processed_nodes_count += 1

            # Update max_color_value with the values from paths ending at u
            for c_val in range(26):
                max_color_value = max(max_color_value, dp[u][c_val])

            for v in adj[u]:
                for c_idx in range(26):
                    # Propagate dp values from u to v
                    # Add 1 if color of v matches c_idx
                    increment = 1 if (ord(colors[v]) - ord('a')) == c_idx else 0
                    dp[v][c_idx] = max(dp[v][c_idx], dp[u][c_idx] + increment)
                
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        if processed_nodes_count < n:
            return -1  # Cycle detected
        else:
            # If n > 0 and no cycle, max_color_value should be at least 1.
            # If processed_nodes_count == n == 0, this part is not hit due to constraints.
            # If n > 0, processed_nodes_count == n, means all nodes were processed.
            # If max_color_value is still 0, it means n > 0 but all dp values remained 0.
            # This is only possible if the initial queue was empty (cycle) or
            # something is wrong. But dp[i][color] = 1 for start nodes.
            # So if n > 0 and processed_nodes_count == n, max_color_value >= 1.
            # However, if n > 0 and there are no edges, and all nodes are processed,
            # max_color_value becomes 1 (from single node paths).
            return max_color_value
