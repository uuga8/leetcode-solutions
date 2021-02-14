class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        answer = []
        
        for index in range(0, len(nums)):
            
            first_half = target - nums[index]
            
            if first_half in seen:
                answer.append(seen[first_half])
                answer.append(index)
                break
            else:
                seen[nums[index]] = index
                
        return answer
