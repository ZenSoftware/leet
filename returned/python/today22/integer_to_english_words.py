# https://leetcode.com/problems/integer-to-english-words/description/
from collections import deque

class Solution:
    initial = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen',
    }
    
    tens = {
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }

    groups = {
        1: 'Thousand',
        2: 'Million',
        3: 'Billion',
        4: 'Trillion',
    }
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        n = str(num)
        result = deque()
        
        hundreds = n[-min(len(n), 3):] 
        if not self.isZeros(hundreds):
            result.append(self.sayHundreds(hundreds))

        for i, group_name in self.groups.items():
            if len(n) > 3*i:
                group = n[-min(len(n), 3*i + 3) : -3*i]
                if not self.isZeros(group):
                    result.appendleft(group_name)
                    result.appendleft(self.sayHundreds(group))

        return ' '.join(result)

    def sayHundreds(self, n: str) -> str:
        n = self.stripLeadingZeros(n)

        result = []

        if len(n) >= 3:
            result.append(self.initial[n[-3]]) 
            result.append('Hundred')

        if not self.isZeros(n[-2:]):
            if int(n[-2:]) < 20:
                tens = self.stripLeadingZeros(n[-2:])
                result.append(self.initial[tens])
            else:
                result.append(self.tens[n[-2:-1]])
                if n[-1] != '0':
                    result.append(self.initial[n[-1]])
        
        return ' '.join(result)

    def isZeros(self, n: str) -> str:
        for c in n:
            if c != '0':
                return False
        return True
    
    def stripLeadingZeros(self, n: str) -> str:
        while n[0] == '0':
            n = n[1:]
        return n