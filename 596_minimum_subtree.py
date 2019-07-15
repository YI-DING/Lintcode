def findSubtree(self, root):
    
    def find(root):
        if not root:
            return None, maxsize, 0
        leftnode, leftsize, leftsum = find(root.left)
        rightnode, rightsize, rightsum = find(root.right)
        rootsum = root.val + leftsum + rightsum
        if leftsize == min(leftsize,rightsize,rootsum):
            return leftnode, leftsize, rootsum
        if rightsize == min(leftsize,rootsum,rightsize):
            return rightnode, rightsize, rootsum
        return root, rootsum, rootsum
    
    node, value, flg = find(root)
    return node