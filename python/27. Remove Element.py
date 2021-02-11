class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right_index = len(nums) -1
        result_length = 0
        
        for left_index in range(0, len(nums)):
            if left_index == right_index + 1:
                break
            if nums[left_index] != val:
                result_length += 1
            else:
                if nums[right_index] != val:
                    nums[left_index] = nums[right_index]
                    right_index -= 1
                    result_length += 1
                else:
                    while left_index < right_index:
                        if nums[right_index] == val:
                            right_index -= 1
                        else:
                            break
                    if left_index == right_index:
                        return result_length
                    else:                
                        nums[left_index] = nums[right_index]
                        right_index -= 1
                        result_length += 1
        return result_length
        
        
