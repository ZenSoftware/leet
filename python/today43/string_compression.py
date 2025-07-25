# https://leetcode.com/problems/string-compression/description/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            letter = chars[read]
            count = 0
            while read < len(chars) and chars[read] == letter:
                count += 1
                read += 1

            chars[write] = letter
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
