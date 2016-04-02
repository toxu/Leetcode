        def helper(ins, ine, posts, poste):
            if ins < 0 or ine < 0 or posts < 0 or poste < 0:
                return None
            if ins > ine or posts > poste:
                return None
            if ins == ine and posts == poste:
                return TreeNode(inorder[ins])
            root = TreeNode(postorder[poste])
            index = inorder.index(postorder[poste])
            inorder_left = (ins, index-1)
            inorder_left_length = index - ins
            inorder_right = (index+1, ine)
            inorder_right_length = ine - index
            postorder_right = (poste-inorder_right_length,poste-1)
            postorder_left = (posts, poste-1-inorder_right_length)
            root.left = helper(inorder_left[0], inorder_left[1], postorder_left[0], postorder_left[1])
            root.right = helper(inorder_right[0], inorder_right[1], postorder_right[0], postorder_right[1])
            return root

        if len(inorder) != len(postorder):
            return None
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        return helper(0, len(inorder)-1, 0, len(postorder)-1)
