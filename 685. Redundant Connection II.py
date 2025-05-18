from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        def is_rooted_tree(current_edges):
            in_degree = [0] * (n + 1)
            adj = [[] for _ in range(n + 1)]
            nodes = set()
            for u, v in current_edges:
                in_degree[v] += 1
                adj[u].append(v)
                nodes.add(u)
                nodes.add(v)

            if not nodes:
                return True

            root_count = 0
            root = -1
            for i in range(1, n + 1):
                if i in nodes and in_degree[i] == 0:
                    root_count += 1
                    root = i

            if root_count != 1 or len(nodes) != n:
                return False

            visited = [False] * (n + 1)
            queue = [root]
            visited[root] = True
            count = 0
            while queue:
                u = queue.pop(0)
                count += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)

            if count != n:
                return False

            for i in range(1, n + 1):
                if i in nodes and in_degree[i] > 1 and i != root:
                    return False

            return True

        for i in range(len(edges) - 1, -1, -1):
            temp_edges = edges[:i] + edges[i+1:]
            if is_rooted_tree(temp_edges):
                return edges[i]

        return []
