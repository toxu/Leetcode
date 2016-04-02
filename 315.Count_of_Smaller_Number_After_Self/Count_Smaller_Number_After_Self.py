class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_count(left_index, left_sub, right_sub):
            len_left = len(left_sub)
            len_right = len(right_sub)
            merge_res = []
            l, r = 0, 0
            for i in range(len_left+len_right):
                if l == len_left:
                    merge_res += right_sub[r:]
                    return merge_res
                if r == len_right:
                    merge_res += left_sub[l:]
                    for j in range(l, len_left):
                        dic[left_index+j] += len_right
                    return merge_res
                if left_sub[l] > right_sub[r]:
                    merge_res.append(right_sub[r])
                    r += 1
                else:
                    merge_res.append(left_sub[l])
                    dic[left_index+l] += len_right-len(right_sub[r:])
                    l += 1
                print dic
            return merge_res
        def helper(left, right):
            if left >= right:
                return [nums[left]]
            mid = left + (right-left) / 2
            left_sub = helper(left, mid)
            right_sub = helper(mid+1, right)
            return merge_count(left, left_sub, right_sub)
        if len(nums) == 0:
            return []
        smaller = []
        dic = {}
        tuple_nums = list(enumerate(nums))
        for i in range(len(nums)):
            dic[i] = 0
        helper(0, len(nums)-1)
        for i in range(len(nums)):
            smaller.append(dic[i])
        return smaller

s = Solution()
print s.countSmaller([2,0,1])
