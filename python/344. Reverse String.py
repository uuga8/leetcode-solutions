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
