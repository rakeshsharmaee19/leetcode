# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack =[root]
        while stack:
            cv=stack.pop()
            if type(cv)!=int and cv:
                if cv.left:
                    stack.append(cv.right)
                    stack.append(cv.val)
                    stack.append(cv.left)
                elif cv.right:
                    stack.append(cv.right)
                    stack.append(cv.val)
                    stack.append(cv.left)
                else:
                    res.append(cv.val)
            elif cv!=None:
                res.append(cv)

        return res
