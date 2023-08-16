# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def __init__(self):
        self.res=[]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr=[]
        if not root:
            return []
        self.checkSm(0,targetSum, root, arr)
        return self.res
    
    def checkSm(self, sm, targetSum, node, arr):
        smValue=sm+node.val
        if not node.left and not node.right:
            if smValue==targetSum:
                arr.append(node.val)
                newarr=copy.deepcopy(arr)
                self.res.append(arr)
                arr.pop()
                return
        else:
            arr.append(node.val)
            if node.left:
                self.checkSm(smValue,targetSum,  node.left, arr)
            if node.right:
                self.checkSm(smValue,targetSum, node.right, arr)
            arr.pop()
        return
