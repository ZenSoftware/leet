# https://leetcode.com/problems/integer-to-english-words/description/

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
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        n = str(num)
        result = []
        hundreds = n[-min(len(n), 3):] 
        if not self.isZeros(hundreds):
            result.append(self.sayHundreds(hundreds))

        if len(n) > 3:
            thousands = n[-min(len(n), 6) : -3]
            if thousands != '000':
                result.insert(0, 'Thousand')
                result.insert(0, self.sayHundreds(thousands))
        
        if len(n) > 6:
            millions = n[-min(len(n), 9) : -6]
            if millions != '000':
                result.insert(0, 'Million')
                result.insert(0, self.sayHundreds(millions))

        if len(n) > 9:
            billions = n[-min(len(n), 12) : -9]
            if billions != '000':
                result.insert(0, 'Billion')
                result.insert(0, self.sayHundreds(billions))

        if len(n) > 12:
            trillions = n[-min(len(n), 15) : -12]
            result.insert(0, 'Trillion')
            result.insert(0, self.sayHundreds(trillions))

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