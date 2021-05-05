class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0;
        int right = 0;
        
        for (int index = 0; index < nums.length; index++) {
            right += nums[index];
        }
        
        int index;
        for (index = 0; index < nums.length; index++) {
            right = right - nums[index];
            if (left == right) {
                return index;
            } else {
                left = left + nums[index];
            }
        }
    return -1;
    }
}
