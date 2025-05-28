import collections
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = collections.defaultdict(list)
        for u, v_node in edges1:
            adj1[u].append(v_node)
            adj1[v_node].append(u)

        adj2 = collections.defaultdict(list)
        for u, v_node in edges2:
            adj2[u].append(v_node)
            adj2[v_node].append(u)

        def run_bfs(start_node: int, num_total_nodes: int, current_adj: collections.defaultdict) -> List[int]:
            dists_from_start = [-1] * num_total_nodes
            if not (0 <= start_node < num_total_nodes):
                 return dists_from_start 
            
            dists_from_start[start_node] = 0
            queue = collections.deque([start_node])
            
            while queue:
                u_node = queue.popleft()
                for v_neighbor in current_adj[u_node]:
                    if 0 <= v_neighbor < num_total_nodes and dists_from_start[v_neighbor] == -1:
                        dists_from_start[v_neighbor] = dists_from_start[u_node] + 1
                        queue.append(v_neighbor)
            return dists_from_start

        d1 = [[-1]*n for _ in range(n)]
        for i in range(n):
            d1[i] = run_bfs(i, n, adj1)

        d2 = [[-1]*m for _ in range(m)]
        for i in range(m):
            d2[i] = run_bfs(i, m, adj2)
        
        targets_in_T1_count = [0] * n
        for s1_node in range(n):
            count = 0
            for t1_node in range(n):
                if d1[s1_node][t1_node] != -1 and d1[s1_node][t1_node] <= k:
                    count += 1
            targets_in_T1_count[s1_node] = count
        
        # count_reachable_in_T2[c2_idx][limit]: num nodes y in T2 s.t. d2[c2_idx][y] <= limit
        # limit is from 0 to m-1
        count_reachable_in_T2 = [[0]*m for _ in range(m)]
        if m > 0: # Ensure m is positive before indexing up to m-1
            for c2_node_outer in range(m):
                nodes_at_each_dist = [0] * m 
                for y_node in range(m):
                    dist_c2_y = d2[c2_node_outer][y_node]
                    if dist_c2_y != -1: 
                        nodes_at_each_dist[dist_c2_y] += 1
                
                current_sum_of_nodes = 0
                for limit in range(m): 
                    current_sum_of_nodes += nodes_at_each_dist[limit]
                    count_reachable_in_T2[c2_node_outer][limit] = current_sum_of_nodes

        # max_nodes_in_T2_for_limit[rem_k_val]: max nodes in T2 reachable with budget rem_k_val
        # rem_k_val is from 0 to k
        max_nodes_in_T2_for_limit = [0] * (k + 1)
        for limit_val_for_T2 in range(k + 1):
            current_max_for_this_limit = 0
            if m == 0: # No nodes in T2
                current_max_for_this_limit = 0
            elif limit_val_for_T2 >= m - 1 : # Max dist in T2 is m-1
                current_max_for_this_limit = m
            else: # 0 <= limit_val_for_T2 < m - 1
                val = 0
                for c2_node_inner in range(m):
                    val = max(val, count_reachable_in_T2[c2_node_inner][limit_val_for_T2])
                current_max_for_this_limit = val
            max_nodes_in_T2_for_limit[limit_val_for_T2] = current_max_for_this_limit
            
        answer = [0] * n
        for s1_node in range(n):
            num_T1_targets = targets_in_T1_count[s1_node]
            max_T2_contribution = 0
            
            for c1_node in range(n):
                dist_s1_c1 = d1[s1_node][c1_node]
                if dist_s1_c1 == -1: continue # Should not happen in a connected tree

                remaining_k_for_T2 = k - dist_s1_c1 - 1
                
                current_T2_contribution_val = 0
                if remaining_k_for_T2 >= 0:
                    current_T2_contribution_val = max_nodes_in_T2_for_limit[remaining_k_for_T2]
                
                max_T2_contribution = max(max_T2_contribution, current_T2_contribution_val)
            
            answer[s1_node] = num_T1_targets + max_T2_contribution
            
        return answer
