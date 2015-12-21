class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, solution, result):
            if not nums:
                result.append(solution)
                return
            preNum = None
            for index, num in enumerate(nums):
                if num == preNum:
                    continue
                preNum = num
                helper(nums[:index]+nums[index+1:], solution + [num], result)
        nums.sort()
        solution = []
        result = []
        helper(nums, solution,result)
        return result

s = Solution()
print s.permute([1,1,2])
