# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(max(len(v1), len(v2))):
            segment1 = 0
            segment2 = 0

            if i < len(v1):
                segment1 = int(v1[i])
            if i < len(v2):
                segment2 = int(v2[i])

            if segment1 < segment2:
                return -1
            elif segment1 > segment2:
                return 1
        
        return 0