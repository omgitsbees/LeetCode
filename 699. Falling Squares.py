import collections

class Solution:
  def fallingSquares(self, positions: list[list[int]]) -> list[int]:
    # This list will store tuples of (left_coord, right_coord_exclusive, top_y_coord)
    # for each square that has landed.
    # The top_y_coord is the y-coordinate of the top surface of the square.
    placed_squares_info = [] 
    
    ans = []
    # max_overall_height tracks the highest y-coordinate reached by the top 
    # of any square on the plane after each drop.
    max_overall_height = 0

    for i in range(len(positions)):
        left_curr, side_len_curr = positions[i]
        right_curr = left_curr + side_len_curr

        # Determine the y-coordinate on which the current square will land.
        # This is the highest top_y_coord of any existing square that the 
        # current square overlaps with horizontally.
        # If it overlaps with none, it lands on the x-axis (y=0).
        base_landing_y = 0
        for prev_left, prev_right, prev_top_y in placed_squares_info:
            # Check for horizontal overlap.
            # Current square's x-interval: [left_curr, right_curr)
            # Previous square's x-interval: [prev_left, prev_right)
            # They overlap if (left_curr < prev_right) AND (prev_left < right_curr).
            # Brushing sides (e.g., left_curr == prev_right or right_curr == prev_left) 
            # does not count as an overlap for landing.
            if left_curr < prev_right and prev_left < right_curr:
                base_landing_y = max(base_landing_y, prev_top_y)
        
        # The top surface of the current square will be at base_landing_y + side_len_curr.
        current_square_top_y = base_landing_y + side_len_curr
        
        # Add information about the newly landed square.
        placed_squares_info.append((left_curr, right_curr, current_square_top_y))
        
        # After this square lands, the new maximum height on the plane is either
        # the previous maximum or the top of this new square, whichever is greater.
        max_overall_height = max(max_overall_height, current_square_top_y)
        ans.append(max_overall_height)
            
    return ans
