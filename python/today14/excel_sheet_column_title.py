# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            result = chr(ord('A') + digit) + result
            columnNumber = (columnNumber - 1) // 26
        return result