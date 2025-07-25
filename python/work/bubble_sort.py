from typing import List
from random import shuffle


def bubble_sort(arr: List):
    for i in range(len(arr) - 1):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


sample = [14, 12, 2, 13, 6, 18, 7, 16, 3, 15, 8, 9, 11, 17, 19, 1, 5, 10, 4, 0]
shuffle(sample)
print(sample)

bubble_sort(sample)
print("sorted", sample)
