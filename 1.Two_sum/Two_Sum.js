/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var dic = {};
    for(i=0;i<nums.length;i++){
    	if(target-nums[i] in dic){
    		return [dic[target-val], i+1];
    	}
    	else{
    		dic[nums[i]] = i+1;
    	}
    }
};