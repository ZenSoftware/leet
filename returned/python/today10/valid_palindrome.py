class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''
        for c in s:
            ascii_val = ord(c)
            # 0 - 9
            if 48 <= ascii_val <= 57:
                stripped += c
            # 'a' - 'z'
            elif 97 <= ascii_val <= 122:
                stripped += c
            # 'A' - 'Z'
            elif 65 <= ascii_val <= 90:
                stripped += c.lower()
                
        l, r = 0, len(stripped) - 1
        while l < r:
            if stripped[l] != stripped[r]:
                return False
            l += 1
            r -= 1
        return True
        