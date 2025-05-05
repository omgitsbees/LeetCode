import math
from typing import List

class Solution:
    """
    Solves the "Erect the Fence" problem using the Monotone Chain algorithm (Andrew's Algorithm)
    to find the convex hull of a set of points (trees).
    """
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """
        Finds the coordinates of trees that are located on the convex hull perimeter.

        Args:
            trees: A list of lists, where each inner list [xi, yi] represents the 
                   coordinates of a tree.

        Returns:
            A list of lists representing the coordinates of trees on the fence perimeter.
            The order of the points is not specified. Collinear points on the hull
            are included.
        """
        n = len(trees)

        # Handle the edge case where there are 3 or fewer trees. 
        # In this case, all unique trees form the convex hull.
        # The problem statement guarantees 1 <= n, and unique positions.
        # So if n <= 2, all points are on the hull. If n = 3, they form a triangle (possibly degenerate)
        # and are all on the hull unless they are collinear. The algorithm handles collinearity.
        # For simplicity and clarity, handle n < 3 explicitly might seem redundant but ensures correctness
        # if the main algorithm had issues with very small inputs.
        # However, the Monotone Chain algorithm works correctly for n >= 1 if implemented carefully.
        # Let's rely on the main algorithm, but add a check for n=0 just in case (though constraints say n>=1).
        if n == 0:
            return []
        if n <= 2:
             return trees # All points are on the hull if n <= 2 (and unique)

        # --- Monotone Chain Algorithm ---

        # 1. Sort points lexicographically: primarily by x-coordinate, secondarily by y-coordinate.
        # Convert points to tuples for easier handling, especially for using sets later.
        points = sorted([tuple(p) for p in trees])

        # 2. Define the orientation function (based on cross product).
        # It determines whether the turn from vector pq to vector qr is
        # counter-clockwise (CCW), clockwise (CW), or collinear.
        def orientation(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
            """
            Calculates the orientation of ordered triplet (p, q, r).
            Args:
                p, q, r: Points represented as tuples (x, y).
            Returns:
                > 0 if the turn at q from pq to qr is Counter-Clockwise (Left turn).
                < 0 if the turn at q from pq to qr is Clockwise (Right turn).
                  0 if p, q, r are collinear.
            """
            # Formula derived from the z-component of the cross product of vectors pq and qr:
            # pq = (qx - px, qy - py)
            # qr = (rx - qx, ry - qy)
            # cross_product_z = (qx - px) * (ry - qy) - (qy - py) * (rx - qx)
            val = (q[1] - p[1]) * (r[0] - q[0]) - \
                  (q[0] - p[0]) * (r[1] - q[1])
            return val

        # 3. Build the lower hull.
        # Iterate through sorted points from left to right.
        # Maintain a stack (list) `lower_hull`.
        # Pop from stack if adding the current point `p` makes a Clockwise turn
        # with the last two points on the stack. This ensures the lower hull is convex.
        # Collinear points are kept.
        lower_hull = []
        for p in points:
            # While stack has at least 2 points and the turn (stack[-2], stack[-1], p) is CW
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) < 0:
                lower_hull.pop()
            lower_hull.append(p) # Add current point

        # 4. Build the upper hull.
        # Iterate through sorted points from right to left (using reversed list).
        # Maintain a stack (list) `upper_hull`.
        # Pop from stack if adding the current point `p` makes a Clockwise turn
        # relative to the reversed traversal direction.
        # Collinear points are kept.
        upper_hull = []
        for p in reversed(points):
            # While stack has at least 2 points and the turn (stack[-2], stack[-1], p) is CW
            # relative to the direction of traversal (right-to-left).
            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) < 0:
                upper_hull.pop()
            upper_hull.append(p) # Add current point

        # 5. Combine the hulls.
        # The final convex hull includes all points from both the lower and upper hulls.
        # Use a set to automatically handle duplicate points (the start and end points
        # of the sorted list will appear in both hulls).
        hull_points_set = set(lower_hull) | set(upper_hull)

        # 6. Convert the set of tuples back to the required list of lists format.
        return [list(p) for p in hull_points_set]
