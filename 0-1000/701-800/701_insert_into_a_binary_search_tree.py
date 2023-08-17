# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        ch=True
        node=root
        while ch:
            vl=node
            if vl.val<val:
                if vl.right:
                    node=vl.right
                else:
                    vl.right=TreeNode(val)
                    ch=False
            else:
                if vl.left:
                    node=vl.left
                else:
                    vl.left=TreeNode(val)
                    ch=False
        return root
