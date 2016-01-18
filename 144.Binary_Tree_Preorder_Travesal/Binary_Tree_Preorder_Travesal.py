# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        node = root
        while node or stack:
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        return res
