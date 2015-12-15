class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, max_square = 0, len(height)-1, 0
        while left < right:
            max_square = max(max_square, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_square