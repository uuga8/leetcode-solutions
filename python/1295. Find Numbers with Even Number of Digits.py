class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        
        for index in range(0, len(nums)):
            if nums[index] >= 10 and nums[index] < 100 or\
                nums[index] >= 1000 and nums[index] < 10000 or\
                nums[index] == 100000:
                even += 1
        return even
        
