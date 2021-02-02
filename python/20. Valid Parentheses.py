class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        if len(s) < 2 or s[0] in close:
            return False
                    
        stack = []
        def checkers(s):
            index = 0
            while index < len(s) and s[index] in open:
                stack.append(s[index])
                index += 1
            while index < len(s) and s[index] in close:
                if stack and close.index(s[index]) == open.index(stack[-1]):
                    stack.pop()
                    index += 1
                else:
                    return False
            if index < len(s) -1:
                return checkers(s[index:])
            if not stack and index == len(s):
                return True
        return checkers(s)
