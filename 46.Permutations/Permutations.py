class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, solution, result):
            if not nums:
                result.append(solution)
                return
            for index, num in enumerate(nums):
                helper(nums[:index]+nums[index+1:], solution + [num], result)
        solution = []
        result = []
        helper(nums, solution,result)
        return result

s = Solution()
print s.permute([1,1,2])
