# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
from random import choice


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        i = self.val_to_index[val]
        self.val_to_index[self.values[-1]] = i
        self.values[i], self.values[-1] = self.values[-1], self.values[i]
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values)
