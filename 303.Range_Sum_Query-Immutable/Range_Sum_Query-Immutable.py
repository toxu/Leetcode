class BinaryIndexTree(object):
    def __init__(self, nums):
        self.bit = [0 for i in range(len(nums)+1)]
        self.length = len(nums)
        for i in range(1, len(nums)+1):
            self.update(i, nums[i-1])
    
    def update(self, index, val):
        while index <= self.length:
            self.bit[index] += val
            index += index & (-index)

    def getSum(self, index):
        s = 0
        index += 1
        while index > 0:
            s += self.bit[index]
            index -= index & (-index)
        return s

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.bit = BinaryIndexTree(nums)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.bit.getSum(j) - self.bit.getSum(i-1)
a = [1,2,3,4]
s = NumArray(a)
print s.sumRange(0,2)
