class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int current = 0;
        int max = 0;
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (nums[i] == 1) {
                current += 1;
            } else {
                max = Math.max(current, max);
                current = 0;
            }
        } return Math.max(max, current);
    }
}
