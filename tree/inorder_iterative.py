def inorder_traversal(root):
    stack = []
    result = []

    if not root:
        return result

    curr_node = root
    while stack or curr_node:
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
    return result
