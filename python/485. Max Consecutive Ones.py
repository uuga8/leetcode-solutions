class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        consecutives = []
        
        for index in range(0, len(nums)):
            if nums[index] == 1:
                count += 1
            if (nums[index] != 1 or index == (len(nums) -1)) and count > 0 :
                consecutives.append(count)
                count = 0
                
        return 0 if not consecutives else max(consecutives)
