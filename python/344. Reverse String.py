class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        for index in range(0, len(s)//2):
            temp = s[index]
            s[index] = s[-index-1]
            s[-index-1] = temp
            
            
            
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        def helper(s, index):
            
            if index == len(s)//2:
                return None
            s[index], s[-index -1] = s[-index -1], s[index]
                
            return helper(s, index + 1)
        helper(s, 0)

        
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(lo, hi):
            if lo < hi:
                s[lo], s[hi] = s[hi], s[lo]
                helper(lo + 1, hi - 1)
        
        helper(0, len(s) - 1)
