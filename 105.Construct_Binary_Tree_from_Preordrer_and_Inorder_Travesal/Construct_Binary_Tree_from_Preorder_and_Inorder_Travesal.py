# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])

            left_tree = inorder[0:index]
            right_tree = inorder[index+1:]
            root.left = helper(preorder[1:1+len(left_tree)], left_tree)
            root.right = helper(preorder[1+(len(left_tree)):], right_tree)
            return root

        if len(preorder)==0 or len(inorder) == 0:
            return None
        return helper(preorder, inorder)

        def helper(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e or in_s > in_e:
                return None
            if pre_s == pre_e:
                return TreeNode(preorder[pre_s])
            root = TreeNode(preorder[pre_s])
            index = inorder[in_s, in_e].index(preorder[pre_s])

            root.left = helper(pre_s+1, pre_s+1 + index-in_s, in_s, index-1)
            root.right = helper(pre_s + 1 + index-in_s+1, pre_e, index+1, in_e)
            return root

        if len(preorder)==0 or len(inorder) == 0:
            return None
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
