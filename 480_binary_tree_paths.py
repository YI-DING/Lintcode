def binaryTreePaths(self, root):
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]
    paths = []
    for path in self.binaryTreePaths(root.left):
        paths.append(str(root.val) + "->" + path)
    for path in self.binaryTreePaths(root.right):
        paths.append(str(root.val) + "->" + path)
    return paths