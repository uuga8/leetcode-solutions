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
            
