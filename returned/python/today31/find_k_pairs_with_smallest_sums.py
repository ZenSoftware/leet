# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
from typing import List
from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or not k:
            return res
        
        visited = set([(0,0)])
        heap = [(nums1[0]+nums2[0], 0, 0)]

        while heap and k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                item = (nums1[i+1]+nums2[j], i+1, j)
                heappush(heap, item)
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                item = (nums1[i]+nums2[j+1], i, j+1)
                heappush(heap, item)
            
            k -= 1
        
        return res