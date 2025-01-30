# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        longest_len = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1 > longest_len):
                    longest = s[l:r+1]
                    longest_len = r-l+1
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1 > longest_len):
                    longest = s[l:r+1]
                    longest_len = r-l+1
                l -= 1
                r += 1

        return longest

