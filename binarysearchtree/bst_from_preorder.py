def rebuild_bst_from_preorder(preorder_sequence):

    if not preorder_sequence:
        return None

    transition_point = next(
        (i
         for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]),
        len(preorder_sequence))
    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:]))