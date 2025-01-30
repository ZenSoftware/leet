# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1 > len(longest)):
                    longest = s[l:r+1]
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1 > len(longest)):
                    longest = s[l:r+1]
                l -= 1
                r += 1

        return longest

