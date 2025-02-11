# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a = len(a) - 1
        index_b = len(b) - 1
        ans = []
        carry = 0
        while index_a >= 0 or index_b >= 0 or carry == 1:
            digit_a, digit_b = 0, 0
            if index_a >= 0:
                digit_a = int(a[index_a])
            if index_b >= 0:
                digit_b = int(b[index_b])

            total = digit_a + digit_b + carry
            if total <= 1:
                ans.append(str(total))
                carry = 0
            else:
                ans.append(str(total % 2))
                carry = 1

            index_a -= 1
            index_b -= 1
        return ''.join(reversed(ans))

        