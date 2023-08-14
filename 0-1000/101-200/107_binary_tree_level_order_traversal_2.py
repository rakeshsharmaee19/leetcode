# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    # case when three is empty
            return []
        visited, queue = [], collections.deque([root])   # create visited and Queue

        while queue:
            queue_length=len(queue) 
            level_visited=[]
            for i in range(queue_length):
                node=queue.popleft()
                level_visited.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            visited.insert(0, level_visited)
        return visited
        
