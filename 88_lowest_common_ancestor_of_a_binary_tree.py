def lowestCommonAncestor(self, root: 'TreeNode', A: 'TreeNode', B: 'TreeNode') -> 'TreeNode':`
    if not root:
        return None
    if A == root or B == root:
        return root
    
    left_result = self.lowestCommonAncestor(root.left,A,B)
    right_result = self.lowestCommonAncestor(root.right,A,B)
    
    if left_result and right_result:
        return root
    if left_result:
        return left_result
    if right_result:
        return right_result
    return None