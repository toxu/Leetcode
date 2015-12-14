class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dic;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
        	if(dic.find(target-val) != dic.end()){
        		res.push_back(dic[target-val]);
        		res.push_back(i+1);
        		return res;
        	}
        	else{
        		dic.insert({val, i+1});
        	}
        }
    }
};