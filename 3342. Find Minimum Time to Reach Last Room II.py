import heapq

class Solution:
  # Renaming the method to match the expected name 'minTimeToReach'
  def minTimeToReach(self, moveTime: list[list[int]]) -> int:
    n = len(moveTime)
    m = len(moveTime[0])

    # dist[r][c][0] stores the minimum time to arrive at cell (r,c)
    # such that the *next* move from (r,c) will cost 1 second.
    # dist[r][c][1] stores the minimum time to arrive at cell (r,c)
    # such that the *next* move from (r,c) will cost 2 seconds.
    
    infinity = float('inf')
    # Initialize distances with infinity
    dist = [[[infinity] * 2 for _ in range(m)] for _ in range(n)]

    # Priority queue stores tuples: (current_arrival_time_at_rc, r, c, k_idx_for_next_move_from_rc)
    # k_idx_for_next_move_from_rc: 0 if the next move from (r,c) costs 1, 1 if it costs 2.
    pq = []

    # Start at (0,0) at time t=0.
    # The first move *from* (0,0) will cost 1 second.
    # So, the time to arrive at (0,0), ready for a 1-second next move, is 0.
    # dist[r][c][0] means next move from (r,c) costs 1.
    dist[0][0][0] = 0
    heapq.heappush(pq, (0, 0, 0, 0)) 

    # Delta row and column for neighbors (Up, Down, Left, Right)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # Costs for moves: actual_move_costs[0] means 1s, actual_move_costs[1] means 2s
    actual_move_costs = [1, 2] 

    while pq:
        current_arrival_time_at_rc, r, c, k_idx_for_next_move_from_rc = heapq.heappop(pq)

        # If we found a shorter path already to this state
        if current_arrival_time_at_rc > dist[r][c][k_idx_for_next_move_from_rc]:
            continue

        # Cost of the move *from* (r,c) to an adjacent neighbor
        cost_of_current_move = actual_move_costs[k_idx_for_next_move_from_rc]
        
        # The state for the neighbor: if current move was 1s (k_idx=0), 
        # the next move from neighbor is 2s (k_idx=1), and vice versa.
        k_idx_for_move_from_neighbor = 1 - k_idx_for_next_move_from_rc

        for i in range(4): # Iterate over four neighbors
            nr, nc = r + dr[i], c + dc[i]

            # Check if the neighbor is within grid boundaries
            if 0 <= nr < n and 0 <= nc < m:
                # current_arrival_time_at_rc is the earliest we are at (r,c) ready for this type of move.
                # This is the earliest time we *could* start moving from (r,c).
                ready_to_depart_from_rc_time = current_arrival_time_at_rc
                
                # Constraint: "moveTime[nr][nc]" is the minimum time when you can *start moving to* (nr,nc)
                min_time_to_initiate_move_to_neighbor = moveTime[nr][nc]
                
                # Effective departure time from (r,c) towards (nr,nc)
                # Must be at least when we arrived at (r,c) AND when movement to (nr,nc) is allowed.
                actual_departure_time = max(ready_to_depart_from_rc_time, min_time_to_initiate_move_to_neighbor)
                
                # Time of arrival at the neighbor (nr,nc)
                arrival_time_at_neighbor = actual_departure_time + cost_of_current_move

                # If this path is shorter to reach (nr,nc) with its specific next move cost state
                if arrival_time_at_neighbor < dist[nr][nc][k_idx_for_move_from_neighbor]:
                    dist[nr][nc][k_idx_for_move_from_neighbor] = arrival_time_at_neighbor
                    heapq.heappush(pq, (arrival_time_at_neighbor, nr, nc, k_idx_for_move_from_neighbor))
    
    # The result is the minimum time to arrive at the destination (n-1, m-1),
    # regardless of what the cost of the move *from* (n-1,m-1) would have been.
    final_time_at_destination = min(dist[n-1][m-1][0], dist[n-1][m-1][1])
    
    # If the destination is unreachable, final_time_at_destination would be infinity.
    if final_time_at_destination == infinity:
        # This case might not be explicitly tested if problems guarantee reachability,
        # but it's good practice.
        return -1 
    
    return int(final_time_at_destination)
