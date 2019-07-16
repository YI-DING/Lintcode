def lowestCommonAncestor3(self, root, A, B):
    def helper(root,A,B):
        if not root:
            return None, False, False

        left_result, both_flag_left, single_left = helper(root.left, A, B)
        right_result, both_flag_right, single_right = helper(root.right, A, B)
        if root in (A,B):
            if left_result or right_result:
                return root, True, False
            else:
                return root, False, True
        if both_flag_right:
            return right_result, True, False
        if both_flag_left:
            return left_result, True, False

        if left_result and right_result:
            return root, True, False
        
        if left_result:
            return left_result, False, True
        if right_result:
            return right_result, False, True

        return None, False, False
    
    result, dum, single = helper(root,A,B)
    return result if not single else None
#answer from @jiuzhang.com:
def lowestCommonAncestor3(self, root, A, B):
    # write your code here
    a, b, lca = self.helper(root, A, B)
    if a and b:
        return lca
    else:
        return None

def helper(self, root, A, B):
    if root is None:
        return False, False, None
        
    left_a, left_b, left_node = self.helper(root.left, A, B)
    right_a, right_b, right_node = self.helper(root.right, A, B)
    
    a = left_a or right_a or root == A
    b = left_b or right_b or root == B
    
    if root == A or root == B:
        return a, b, root

    if left_node is not None and right_node is not None:
        return a, b, root
    if left_node is not None:
        return a, b, left_node
    if right_node is not None:
        return a, b, right_node

    return a, b, None