# https://leetcode.com/problems/license-key-formatting/description/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        characters = s.replace("-", "")
        characters = characters.upper()
        first_block_len = len(characters) % k
        if first_block_len == 0:
            first_block_len = k
        first_block = characters[:first_block_len]

        blocks = [first_block]
        for i in range(first_block_len, len(characters), k):
            block = characters[i : i + k]
            blocks.append(block)

        return "-".join(blocks)
