# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        for p1_end in range(len(num)-2):
            for p2_end in range(p1_end+1, len(num)-1):
                prev1 = num[:p1_end+1]
                if prev1[0] == '0' and len(prev1) > 1:
                    return False

                prev2 = num[p1_end+1 : p2_end+1]
                if prev2[0] == '0' and len(prev2) > 1:
                    break
                
                if self.valid(num, int(prev1), int(prev2), p2_end+1):
                    return True
        
        return False
    
    def valid(self, num: str, prev1: int, prev2: int, i: int):
        while i < len(num):
            total = prev1 + prev2
            string_total = str(total)
            next_num = num[i : i+len(string_total)]
            if next_num != string_total:
                return False
            prev1 = prev2
            prev2 = total
            i += len(string_total)

        return True