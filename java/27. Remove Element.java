class Solution {
    public int removeElement(int[] nums, int val) {
        
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            if (nums[left] != val) {
                left += 1;
            } 
            
            else {
                while (left <= right && nums[right] == val) {
                    right -= 1;
                }
                if (left < right) {
                nums[left] = nums[right];
                left += 1;
                right -= 1;           
                }
            }
        } 
        return left;
    }
}
