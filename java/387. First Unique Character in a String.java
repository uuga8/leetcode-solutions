class Solution {
    public int firstUniqChar(String s) {
        String duplicates = "";  
        String temp = "";
        int index = 0;  
        int length = s.length();
        for (index = 0; index < length; index++) {
            temp = s.substring(index, index + 1);
            if (duplicates.indexOf(temp) == -1) {
                if (s.substring(index + 1, length).indexOf(temp) != -1) {
                    duplicates += temp;
            }
                else {
                    break;
         }} 
    }   if (index < length) {
            return s.indexOf(temp);
        }
        else {
            return -1;
}
}}
