from typing import List

def quick_sort(arr: List) -> List:
    def sort(start: int, end: int):
        if start >= end:
            return

        i = start-1
        for j in range(start,end):
            if arr[j] < arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i = i+1
        arr[i], arr[end] = arr[end], arr[i]

        sort(start, i-1)
        sort(i+1, end)

    sort(0, len(arr)-1)
    return arr