class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0
        height.append(-1)
        height.insert(0, -1)
        stack = []
        maxS = 0
        for i in range(0, len(height)):
        	while stack and height[stack[-1]] >= height[i]:
        		index = stack.pop(-1)
        		if height[index] > height[i]:
        			maxS = max(maxS, height[index]*(i-stack[-1]))
        	stack.append(i)

        height.pop(0)
        height.pop(-1)
        return maxS

s = Solution()
print s.largestRectangleArea([1,1])
