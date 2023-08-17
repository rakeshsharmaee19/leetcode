# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx, val in enumerate(inorder)}
        preorder_idx=0

        def treeHelper(left, right):
            nonlocal preorder_idx
            if left>right:
                return None

            node_val = preorder[preorder_idx]
            root=TreeNode(node_val)
            preorder_idx+=1

            inorder_index=inorder_map[node_val]

            root.left = treeHelper(left, inorder_index-1 )
            root.right = treeHelper(inorder_index+1, right)

            return root

        return treeHelper(0, len(inorder)-1)
