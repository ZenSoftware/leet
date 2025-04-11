# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
from random import randint


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.arr.append(val)
        self.index_map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        i = self.index_map[val]
        self.index_map[self.arr[-1]] = i
        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
        self.arr.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        r = randint(0, len(self.arr) - 1)
        return self.arr[r]
