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

    
    
    
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 0
        highest_count = 0
        
        for index in range(0, len(nums)):
            if nums[index] == 1:
                current_count += 1
            if (nums[index] != 1 or index == len(nums) - 1) and current_count > 0:
                if current_count > highest_count:
                    highest_count = current_count
                current_count = 0
        return highest_count
