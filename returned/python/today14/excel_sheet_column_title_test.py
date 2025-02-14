from excel_sheet_column_title import Solution

def test1():
    assert Solution().convertToTitle(1) == 'A'

def test2():
    assert Solution().convertToTitle(28) == 'AB'

def test3():
    assert Solution().convertToTitle(701) == 'ZY'