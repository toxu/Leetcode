# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         import heapq
#         heapq.heapify(nums)
#         return heapq.nlargest(k, nums)[-1]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos = self.partion(nums, 0, len(nums)-1)
        if k > len(nums[pos:]):
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif k < len(nums[pos:]):
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]

    def partion(self, nums, left, right):
        pivot = nums[right]
        lo = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[right] = nums[right], nums[lo]
        return lo


s = Solution()
print s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
