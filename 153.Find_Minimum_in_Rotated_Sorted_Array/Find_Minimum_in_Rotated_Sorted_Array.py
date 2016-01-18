class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = (end-start)/2 + start
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
