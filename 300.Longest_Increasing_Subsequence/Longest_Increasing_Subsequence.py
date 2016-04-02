#class Solution(object):
#    def lengthOfLIS(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        def helper(last, nums):
#            if len(nums) == 0:
#                return 0
#            if len(nums) == 1:
#                return 1 if last < nums[0] else 0
#            if last > nums[0]:
#                return 0
#            else:
#                max_n = 0
#                for i in range(1, len(nums)):
#                    n = helper(nums[0], nums[i:])
#                    max_n = max(max_n, n)
#                return 1+max_n
#        global_max = 0
#        for i in range(len(nums)):
#            local_max = helper(nums[i], nums[i:])
#            global_max = max(global_max, local_max)
#        return global_max

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i] = dp[i-1]+1 if dp[i] < last else dp[i-1]
        """
        l = len(nums)
        dp = [1 for i in range(l)]
        for x in range(l):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y]+1)
        return max(dp) if dp else 0

s = Solution()
print s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
                
