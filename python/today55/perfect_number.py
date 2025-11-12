class Solution(object):
    def checkPerfectNumber(self, num):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num
