# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        root_stack=[root]
        while root_stack:
            root_value=root_stack.pop()
            if root_value:
                res.append(root_value.val)
                root_stack.append(root_value.right)
                root_stack.append(root_value.left)
        return res
