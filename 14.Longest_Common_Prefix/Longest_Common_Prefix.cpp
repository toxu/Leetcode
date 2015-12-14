class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() <= 0){
            return "";
        }
        int min_len = INT_MAX;
        for(int i=0;i<strs.size();i++){
            min_len = min(int(strs[i].length()), min_len);
        }
        for(int i=0;i<min_len;i++){
            int val = strs[0][i];
            for(int j=1;j<strs.size();j++){
                if(strs[j][i] != val){
                    return strs[0].substr(0,i);
                }
            }
        }
        return strs[0].substr(0, min_len);
    }
};