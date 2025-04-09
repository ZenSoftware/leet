# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
from typing import List
from random import uniform
from math import sqrt


class Solution:
    """
    Time: O(1)
    Space: O(1)
    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.radius_squared = radius**2
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        x = uniform(-self.radius, self.radius)
        max_y = sqrt(self.radius_squared - x**2)
        y = uniform(-max_y, max_y)
        x += self.x_center
        y += self.y_center
        return [x, y]
