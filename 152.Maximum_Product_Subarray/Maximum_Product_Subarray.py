class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = local_min = global_max = nums[0]
        for n in nums[1:]:
            tmp = local_max
            local_max = max(local_max*n, local_min*n, n)
            local_min = min(tmp*n, local_min*n, n)
            global_max = max(global_max, local_max)
            print local_max, local_min, global_max
        return global_max

s = Solution()
print s.maxProduct([-4, -3, -2])
