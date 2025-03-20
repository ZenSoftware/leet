from typing import List

def kth_largest(arr: List, k: int) -> int:
    goal = len(arr) - k

    def quick_select(start: int, end: int) -> int:
        '''
        Time: O(logn)
        Space: O(1)
        '''
        i = start - 1
        for j in range(start, end):
            if arr[j] < arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[end] = arr[end], arr[i]

        if i > goal:
            return quick_select(start, i-1)
        elif i < goal:
            return quick_select(i+1, end)
        else:
            return arr[i]
            
    return quick_select(0, len(arr)-1)