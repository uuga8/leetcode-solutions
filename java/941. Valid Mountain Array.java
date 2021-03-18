class Solution {
    public boolean validMountainArray(int[] arr) {
        
        int length = arr.length;
        
        if (length < 3) {
            return false;
        }
        
        int i = 0;
        
        while (i < length -2 && arr[i] < arr[i + 1]) {
            i += 1;
        }
        
        if (i > 0) {
            while (i < length -1 && arr[i] > arr[i + 1]) {
                i += 1;
            }
            
            if (i == length -1) {
                return true;
            }
        }
        return false;
    }
}
