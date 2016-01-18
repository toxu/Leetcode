# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        last_visited = None
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                pre = stack[-1]
                if pre.right and pre.right != last_visited:
                    node = pre.right
                else:
                    tmp = stack.pop()
                    res.append(tmp.val)
                    last_visited = tmp
        return res
