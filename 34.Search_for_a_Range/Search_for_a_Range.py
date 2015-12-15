class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
        	mid = (left + right) / 2
        	if nums[mid] == target:
        		l = mid - 1
        		r = mid + 1
        		while l >= 0:
        			if nums[l] != target:
        				break
        			l -= 1
        		while r < len(nums):
        			if nums[r] != target:
        				break
        			r +=1
        		r -= 1
        		l += 1
        		return [l,r]
        	if nums[mid] < target:
        		left += 1
        	if nums[mid] > target:
        		right -= 1
        return [-1,-1]

s = Solution()
print s.searchRange([1], 1)