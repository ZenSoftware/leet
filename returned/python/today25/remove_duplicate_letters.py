# https://leetcode.com/problems/remove-duplicate-letters/description/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_position = {char: i for i, char in enumerate(s)}
        seen = set()
        string_builder = []

        for i, char in enumerate(s):
            if char not in seen:
                while (string_builder and
                       string_builder[-1] > char and
                       i < last_position[string_builder[-1]]):
                    seen.remove(string_builder[-1])
                    string_builder.pop()
                seen.add(char)
                string_builder.append(char)

        return ''.join(string_builder)