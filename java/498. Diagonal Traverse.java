class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int resultLength = (m * n);
        int[] result = new int[resultLength];
        int listIndex = 0;
        int elementIndex = 0;
        int resultIndex = 0;
            
        result[resultIndex] = mat[listIndex][elementIndex];
        resultIndex += 1;
        listIndex -= 1;
        elementIndex += 1;
        
        while (resultIndex < resultLength) {
            if (listIndex < 0 || elementIndex == n) { // you're at the top or end of row
                if (listIndex < 0 && elementIndex < n) {
                    listIndex += 1;
                }
                
                if (elementIndex == n) {
                    listIndex += 2;
                    elementIndex -= 1;
                }
                result[resultIndex] = mat[listIndex][elementIndex];
                resultIndex += 1;
                elementIndex -= 1;
                listIndex += 1;
                
                while (listIndex < m && elementIndex >= 0) { // going down
                    result[resultIndex] = mat[listIndex][elementIndex];
                    resultIndex += 1;
                    elementIndex -= 1;
                    listIndex += 1;
                }
                
            }
            
            else { // you're at the bottom or beginning of row
                if (listIndex == m) {
                    listIndex -= 1;
                    elementIndex += 2;
                }
                if (elementIndex < 0) {
                    elementIndex += 1;
                }
                result[resultIndex] = mat[listIndex][elementIndex];
                resultIndex += 1;
                elementIndex += 1;
                listIndex -= 1;
                
                while (listIndex >= 0 && elementIndex < n) { // going up
                    result[resultIndex] = mat[listIndex][elementIndex];
                    resultIndex += 1;
                    elementIndex += 1;
                    listIndex -= 1;
                }
            }
        }
        return result;
    }
}
