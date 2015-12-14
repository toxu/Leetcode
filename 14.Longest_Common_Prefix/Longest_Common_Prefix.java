public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length <= 0){
            return "";
        }
        int min_len = Integer.MAX_VALUE;
        for(int i=0;i<strs.length;i++){
            min_len = Math.min(strs[i].length(), min_len);
        }
        for(int i=0;i<min_len;i++){
            char val = strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                if(strs[j].charAt(i) != val){
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0].substring(0,min_len);
    }
}