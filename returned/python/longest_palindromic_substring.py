# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        def calc_pal(l: int, r: int):
            nonlocal longest
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1 > len(longest)):
                   longest = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            calc_pal(i,i)   # odd length
            calc_pal(i,i+1) # even length

        return longest
