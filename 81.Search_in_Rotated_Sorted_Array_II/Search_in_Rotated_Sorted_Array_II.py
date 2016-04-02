class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid  + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
