# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ans = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

        for i in range(len(word1)):
            ans[i][len(word2)] = len(word1) - i
        for j in range(len(word2)):
            ans[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    ans[i][j] = ans[i+1][j+1]
                else:
                    ans[i][j] = 1 + min(ans[i+1][j], ans[i][j+1], ans[i+1][j+1])

        return ans[0][0]