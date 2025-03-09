from typing import List

def combinations(nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[]]
    
    firstEl = nums[0]
    withoutFirst = nums[1:]
    combsWithoutFirst = combinations(withoutFirst)
    combsWithFirst = []

    for comb in combsWithoutFirst:
        combWithFirst = [firstEl] + comb
        combsWithFirst.append(combWithFirst)
    
    return combsWithFirst + combsWithoutFirst

print(combinations([1,2,3,4]))