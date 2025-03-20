from typing import List

def quick_sort(elements: List) -> List:
    def sort(start: int, end: int):
        if start >= end:
            return

        i = start-1
        for j in range(start,end):
            if elements[j] < elements[end]:
                i += 1
                elements[i], elements[j] = elements[j], elements[i]

        i = i+1
        elements[i], elements[end] = elements[end], elements[i]

        sort(start, i-1)
        sort(i+1, end)
    sort(0, len(elements)-1)
    return elements