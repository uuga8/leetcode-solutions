class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        stack_top_index = -1
        result = []
        next_index = 0
    
        if nums[0] < 0 and nums[-1] > 0:
            while nums[next_index] < 0:
                next_index += 1
                stack_top_index += 1
            while nexat_index < len(nums) and stack_top_index >= 0:
                if nums[next_index] > abs(nums[stack_top_index]):
                    result.append(nums[stack_top_index]**2)
                    stack_top_index -= 1
                else:
                    result.append(nums[next_index]**2)
                    next_index += 1
            if stack_top_index < 0 and next_index < len(nums):
                for index in range(next_index, len(nums)):
                    result.append(nums[index]**2)
            if stack_top_index >= 0 and next_index == len(nums):
                while stack_top_index >= 0:
                    result.append(nums[stack_top_index]**2)
                    stack_top_index -= 1

        elif nums[0] >= 0:
            for index in range(0, len(nums)):
                result.append(nums[index]**2)
        else:
            if nums[-1] <= 0:
                for index in range(-1, -len(nums) -1, -1):
                    result.append(nums[index]**2)
        return result
