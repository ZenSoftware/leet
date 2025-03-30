from typing import List


def bisect_return_right(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # (right-left)//2 + left
        if target < arr[mid]:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return right
