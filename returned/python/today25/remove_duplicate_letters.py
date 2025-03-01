# https://leetcode.com/problems/remove-duplicate-letters/description/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_position = {c: i for i, c in enumerate(s)}
        seen = set()
        result = []

        for i, c in enumerate(s):
            if c not in seen:
                while result and result[-1] > c and i < last_position[result[-1]]:
                    seen.remove(result[-1])
                    result.pop()
                seen.add(c)
                result.append(c)

        return ''.join(result)