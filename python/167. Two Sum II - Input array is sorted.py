class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        index = 0
        
        while index < len(numbers):
            
            first_half = target - numbers[index]
            
            if first_half > numbers[index] or seen.get(first_half, None) == None:
                seen[numbers[index]] = index
                index += 1
            else:
                return [seen[first_half] + 1, index + 1]
 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
           
        right = len(numbers) - 1
        left = 0
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
                
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
           
        right = len(numbers) - 1
        left = 0
        
        while left < right:
            first_half = target - numbers[right]
            if first_half > numbers[left]:
                left += 1
            elif first_half < numbers[left]:
                right -= 1
            else:
                return [left + 1, right + 1]

