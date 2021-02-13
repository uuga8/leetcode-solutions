class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index = 1
        
        if len(nums) == 0:
            return 0
        
        for right_index in range(1, len(nums)):
            if nums[right_index] > nums[left_index-1]:
                nums[left_index] = nums[right_index]
                left_index += 1
        return left_index
