public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dic = new HashMap<Integer, Integer>();
        int[] defaultResult = {0, 0};
        for(int i=0;i<nums.length;i++){
        	if(dic.get(target-nums[i]) != null){
        		int[] res = {dic.get(target-nums[i]), i+1};
        		return res;
        	}
        	else{
        		dic.put(nums[i], i+1);
        	}
        }
        return defaultResult;
    }
}