class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = global_max = nums[0]
        for n in nums[1:]:
            local_max = max(n, local_max + n)
            global_max = max(local_max, global_max)
        return global_max

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# dp[i] = max(dp[i-1]+nums[i], nums[i])
