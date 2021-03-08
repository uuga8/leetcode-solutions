class Solution {
    public boolean isPalindrome(String s) {
        
        
        int length = s.length();
             
        String alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890";
        String copy = new String("");
        
             
        s = s.toLowerCase();
        
        for (int index = 0; index < length; index++) {
            if (alphanumeric.indexOf(s.charAt(index)) > -1) {
                copy += s.charAt(index);
            }
        }
            
        if (copy.length() <= 1) {
            return true;
            }
            
        int lo = 0;
        int hi = copy.length() - 1;
        while (lo <= hi) {
                if (copy.charAt(lo) == copy.charAt(hi)) {
                    lo += 1;
                    hi -= 1;
                } else {
                    return false;
                }
        } return true;
    } 
}
