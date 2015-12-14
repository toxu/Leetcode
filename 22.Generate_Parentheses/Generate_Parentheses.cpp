class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        helper(n, 0, "", res);
        return res;
    }
    
    void helper(int n, int position, string solution, vector<string> &result){
        if(position == 2*n){
            if(isValid(n, solution)){
                result.push_back(solution);
            }
            return;
        }
        if(isValid(n, solution)){
            helper(n, position+1, solution + '(', result);
            helper(n, position+1, solution + ')', result);
        }
        return;
    }
    
    bool isValid(int n, string s){
        int sum = 0;
        int pos_neg = 0;
        for(auto ch: s){
            if(ch == '('){
                sum += 1;
                pos_neg += 1;
            }
            if(ch == ')')
                pos_neg += -1;
            if(pos_neg < 0)
                return false;
        }
        return sum <= n;
    }
};