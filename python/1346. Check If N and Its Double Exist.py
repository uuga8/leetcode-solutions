class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if len(arr) < 2:
            return False
        
        for index in range(1, len(arr)):
            if arr[0] == (2 * arr[index]) or arr[0] == (arr[index] / 2):
                return True 
                
                                    
        return self.checkIfExist(arr[1:])

    
    
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        seen = {}
                
        for index in range(0, len(arr)):
            
            double = arr[index] * 2
            half = arr[index] / 2
            
            if double in seen or half in seen:
                return True
            else:
                seen[arr[index]] = 1
        return False
    
    
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        seen = set()
                
        for index in range(0, len(arr)):
            
            double = arr[index] * 2
            half = arr[index] / 2
            
            if double in seen or half in seen:
                return True
            else:
                seen.add(arr[index])
        return False
