from integer_to_english_words import Solution

def test1():
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"

def test2():
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"

def test3():
    assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

def test4():
    assert Solution().numberToWords(0) == 'Zero'
    assert Solution().numberToWords(1) == 'One'
    assert Solution().numberToWords(2) == 'Two'
    assert Solution().numberToWords(3) == 'Three'
    assert Solution().numberToWords(4) == 'Four'
    assert Solution().numberToWords(5) == 'Five'
    assert Solution().numberToWords(6) == 'Six'
    assert Solution().numberToWords(7) == 'Seven'
    assert Solution().numberToWords(8) == 'Eight'
    assert Solution().numberToWords(9) == 'Nine'
    assert Solution().numberToWords(10) == 'Ten'
    assert Solution().numberToWords(11) == 'Eleven'
    assert Solution().numberToWords(12) == 'Twelve'
    assert Solution().numberToWords(13) == 'Thirteen'
    assert Solution().numberToWords(14) == 'Fourteen'
    assert Solution().numberToWords(15) == 'Fifteen'
    assert Solution().numberToWords(16) == 'Sixteen'
    assert Solution().numberToWords(17) == 'Seventeen'
    assert Solution().numberToWords(18) == 'Eighteen'
    assert Solution().numberToWords(19) == 'Nineteen'
    assert Solution().numberToWords(20) == 'Twenty'
    assert Solution().numberToWords(21) == 'Twenty One'
    assert Solution().numberToWords(30) == 'Thirty'
    assert Solution().numberToWords(31) == 'Thirty One'
    assert Solution().numberToWords(100) == 'One Hundred'
    assert Solution().numberToWords(101) == 'One Hundred One'
    assert Solution().numberToWords(131) == 'One Hundred Thirty One'
    assert Solution().numberToWords(1000) == 'One Thousand'
    assert Solution().numberToWords(4131) == 'Four Thousand One Hundred Thirty One'
    assert Solution().numberToWords(999_004_131) == 'Nine Hundred Ninety Nine Million Four Thousand One Hundred Thirty One'
    assert Solution().numberToWords(1_999_004_131) == 'One Billion Nine Hundred Ninety Nine Million Four Thousand One Hundred Thirty One'