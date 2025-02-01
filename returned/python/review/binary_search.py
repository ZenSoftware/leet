def binary_search(elements, target):
    def bs(left, right):
        mid = (left + right) // 2
        
        if target == elements[mid]:
            return mid
        elif left > right:
            return -1
        
        if target < elements[mid]:
            return bs(left, mid-1)
        else:
            return bs(mid+1, right)

    return bs(0,len(elements)-1)
        