class Solution {
    public void moveZeroes(int[] nums) {
        
        int left = 0;
        int right = 0;
        int length = nums.length;
        
        while (right < length && nums[right] != 0) {
            left += 1;
            right += 1;
        }
        
        
        while (left < length) {
            if (nums[left] == 0) {
                while (right < length && nums[right] == 0) {
                    right += 1;
                }
                if (right < length) {
                    int temp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = temp;
                    left += 1;
                    right += 1;
                }
                else {
                    break;
                }
            }
            else {
                left += 1;
            }
        }
    }
}
