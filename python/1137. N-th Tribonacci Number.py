class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {0: 0, 1: 1, 2:1}
        for key in range(3, n+1):
            memory[key] = memory[key-1] + memory[key-2] + memory[key-3]
        
        return memory[n]

    
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n < 3:
            return 1
        else:
            zero = 0
            one = 1
            two = 1
            for key in range(3, n + 1):
                next = zero + one + two
                zero = one
                one = two
                two = next
            return next
