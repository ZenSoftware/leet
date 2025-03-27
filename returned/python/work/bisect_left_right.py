from typing import List


def bisect_left(arr: List, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def bisect_right(arr: List, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left
