class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        res = 0
        mininum = 0
        while slow < len(height):
        	if(height[slow] == 0):
        		slow += 1
        		continue
        	mininum = height[slow]
        	fast = slow + 1
        	while(fast < len(height)):
        		if(height[fast] < mininum):
        			mininum = min(height[fast], mininum)
        			fast += 1
        		else:
        			h = min(height[slow], height[fast])
        			w = fast - slow -1
        			res = w * h - sum(height[slow+1:fast])
        			print slow,fast,res
        			slow = fast
        			break
        	if(fast == len(height)):
        		slow += 1
        return res

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])

