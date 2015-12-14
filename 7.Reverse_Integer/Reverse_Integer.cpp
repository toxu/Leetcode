class Solution {
public:
    int reverse(int x) {
        if(x == INT_MIN){
            return 0;
        }
        int res = 0;
        int absolute = abs(x);
        while(absolute > 0){
            if(res > INT_MAX/10){
                return 0;
            }
            int val = absolute % 10;
            absolute /= 10;
            res = res*10 + val;
        }
        return x > 0? res: -res;
    }
};