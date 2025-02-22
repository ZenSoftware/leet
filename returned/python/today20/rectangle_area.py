# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        intersection_x = min(ax2, bx2) - max(ax1, bx1)
        intersection_y = min(ay2, by2) - max(ay1, by1)
        intersection_area = intersection_x * intersection_y
        intersection_area = max(0, intersection_area)

        def area(cx1, cy1, cx2, cy2):
            return (cx2 - cx1) * (cy2 - cy1)
        
        return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - intersection_area