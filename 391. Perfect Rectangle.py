from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Calculate the total area and track corners
        total_area = 0
        corner_set = set()
        
        # Bounding rectangle coordinates
        x_min, y_min = float('inf'), float('inf')
        x_max, y_max = float('-inf'), float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            # Update total area
            total_area += (x2 - x1) * (y2 - y1)
            
            # Update bounding rectangle
            x_min, y_min = min(x_min, x1), min(y_min, y1)
            x_max, y_max = max(x_max, x2), max(y_max, y2)
            
            # Track corners
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corner_set:
                    corner_set.remove(corner)
                else:
                    corner_set.add(corner)
        
        # Calculate bounding rectangle area
        bounding_area = (x_max - x_min) * (y_max - y_min)
        
        # Check total area and corner set
        return total_area == bounding_area and corner_set == {(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)}
