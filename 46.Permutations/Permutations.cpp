class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
          vector<int> solution;
          vector<vector<int> > result;
          helper(nums, solution, result);
          return result;
    }

    void helper(vector<int> nums, vector<int> solution, vector<vector<int> > &result){
      if(nums.size() == 0){
        result.push_back(solution);
        return;
      }
      for(int i=0;i<nums.size();i++){
        int tmp = nums[i];
        nums.erase(nums.begin() + i);
        solution.push_back(tmp);
        helper(nums, solution, result);
        solution.pop_back();
        nums.insert(nums.begin() + i, tmp);
      }
    }
};
