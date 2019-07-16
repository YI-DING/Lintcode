def kthSmallest(self, root, k):
    node = TreeNode(10)
    node.right = root
    stack = [node]
    for _ in range(k):
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if not stack:
            break
    return stack[-1].val