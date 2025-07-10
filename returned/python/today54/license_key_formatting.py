# https://leetcode.com/problems/license-key-formatting/description/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "")
        chars = chars.upper()
        first_block_len = len(chars) % k
        if first_block_len == 0:
            first_block_len = k
        first_block = chars[:first_block_len]

        blocks = [first_block]
        for i in range(first_block_len, len(chars), k):
            block = chars[i : i + k]
            blocks.append(block)

        return "-".join(blocks)
