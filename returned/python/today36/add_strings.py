# https://leetcode.com/problems/add-strings/description/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1 = len(num1)-1
        i2 = len(num2)-1
        result = []
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry > 0:
            d1 = 0
            if i1 >= 0:
                d1 = int(num1[i1])
            
            d2 = 0
            if i2 >= 0:
                d2 = int(num2[i2])
            
            place = d1 + d2 + carry
            if place >= 10:
                result.append(str(place - 10))
                carry = 1
            else:
                result.append(str(place))
                carry = 0

            i1 -= 1
            i2 -= 1

        return ''.join(reversed(result))