# https://leetcode.com/problems/bulls-and-cows/description/
from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_counter = defaultdict(int)
        guess_without_bulls = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counter[secret[i]] += 1
                guess_without_bulls.append(guess[i])
        
        cows = 0
        for g in guess_without_bulls:
            if secret_counter[g] > 0:
                cows += 1
                secret_counter[g] -= 1
        
        return f'{bulls}A{cows}B'