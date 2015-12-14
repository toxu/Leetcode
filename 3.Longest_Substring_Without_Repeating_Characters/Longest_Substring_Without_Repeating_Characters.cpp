class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size()==0)
            return 0;
        unordered_set<int> key;
        int b = 0;
        int e = 0;
        int maxlen = 0;
        while(e<s.size()){
            while(key.find(s[e])==key.end() && e<s.size()){
                key.insert(s[e]);
                e++;
            }
            if(e>=s.size())
            {
                maxlen = max(maxlen,e-b);
                break;
            }
            while(e<s.size() && key.find(s[e]) != key.end()){
                maxlen = max(maxlen,e-b);
                key.erase(s[b]);
                b++;
            }
        }
        return maxlen;
    }
};

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() <= 1){
            return s.size();
        }
        int start, end = 0;
        int max_len = 0;
        unordered_map<int, int> dic;
        while(end < s.size()){
            if(dic.find(s[end]) == dic.end()){
                dic[s[end]] = end;
                end++;
            }
            else{
                max_len = max(max_len, end-start);
                start = end = dic[s[end]] + 1;
                dic.clear();
            }
        }
        max_len = max(max_len, end-start);
        return max_len;
    }
};