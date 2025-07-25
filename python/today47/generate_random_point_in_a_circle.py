# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
from typing import List
from random import uniform, random
from math import sqrt, pi, cos, sin


class Solution:
    """
    Time: O(1)
    Space: O(1)
    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = self.radius * sqrt(uniform(0, 1))
        theta = random() * 2 * pi
        return [self.x_center + cos(theta) * r, self.y_center + sin(theta) * r]
