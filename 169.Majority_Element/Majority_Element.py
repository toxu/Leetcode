#class Solution(object):
#    def majorityElement(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        if len(nums) < 1:
#            return -1
#        candidate = nums[0]
#        count = 1
#        for num in nums[1:]:
#            if candidate == num:
#                count += 1
#            elif candidate != num:
#                count -= 1
#                if count <= 0:
#                    candidate = num
#                    count = 1
#        count = 0
#        for num in nums:
#            if num == candidate:
#                count += 1
#        if count > len(nums) / 2:
#            return candidate
#        else:
#            return -1
class Solution(object):
    def majorityElement(self, nums):
        def checkMajor(candidate, nums):
            count = 0
            for num in nums:
                if candidate == num:
                    count += 1
            return count > len(nums) / 2
        if len(nums) == 1:
            return nums[0]
        else:
            mid = len(nums)/2
            left = self.majorityElement(nums[0:mid])
            right = self.majorityElement(nums[mid:])
            if left == right:
                return left
            else:
                if checkMajor(left, nums):
                    return left
                else:
                    return right


s = Solution()
nums = [47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,16,47,36,47,41,19,80,47,47,27]
print s.majorityElement(nums)

        
