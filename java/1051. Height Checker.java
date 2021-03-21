class Solution {
    public int heightChecker(int[] heights) {
        int length = heights.length;
        int[] sorted = Arrays.copyOf(heights, length);
        
        Arrays.sort(sorted);
        
        int count = 0;
        
        for (int i = 0; i < length; i++) {
            if (heights[i] != sorted[i]) {
                count += 1;
            }
        }
        return count;
    }
}
