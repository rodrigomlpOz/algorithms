def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter, None)
        if subtree_key is None:
            return None

        # Note that reconstruct_preorder_helper updates preorder_iter. So the
        # order of following two calls are critical.
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(preorder))
