# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/
from typing import List
import random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        areas = []
        total_area = 0
        for i in range(len(rects)):
            area = (rects[i][2] - rects[i][0]) * (rects[i][3] - rects[i][1])
            areas.append(area)
            total_area += area

        self.percentages = []
        for i in range(len(rects)):
            self.percentages.append(areas[i] / total_area)

    def pick(self) -> List[int]:
        rand = random.random()
        total = 0
        rect = None
        for i in range(len(self.rects)):
            total += self.percentages[i]
            if total > rand:
                rect = self.rects[i]
                break

        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]
