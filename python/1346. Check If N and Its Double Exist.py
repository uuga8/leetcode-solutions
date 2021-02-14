class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if len(arr) < 2:
            return False
        
        for index in range(1, len(arr)):
            if arr[0] == (2 * arr[index]) or arr[0] == (arr[index] / 2):
                return True 
                
                                    
        return self.checkIfExist(arr[1:])
