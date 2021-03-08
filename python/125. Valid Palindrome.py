class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        length = len(s)
        
        alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
        copy = ""
        
        s = s.lower()
        
        for index in range(0, length):
            if s[index] in alphanumeric:
                copy += s[index]
        
        if len(copy) <= 1:
            return True
        
        lo = 0
        hi = len(copy) - 1
        
        while lo <= hi:
            if copy[lo] == copy[hi]:
                lo += 1
                hi -= 1
            else:
                return False

        return True
