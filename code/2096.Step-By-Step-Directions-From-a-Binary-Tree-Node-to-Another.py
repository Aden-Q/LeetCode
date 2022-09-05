# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToDest = []
        path = []
        
        def traverse(root: Optional[TreeNode]):
            nonlocal pathToStart, pathToDest, startValue, destValue, path
            if not root:
                return
            
            if root.val == startValue:
                pathToStart = path[:]
            elif root.val == destValue:
                pathToDest = path[:]
            
            path.append('L')
            traverse(root.left)
            path.pop()
            
            path.append('R')
            traverse(root.right)
            path.pop()
            
        traverse(root)
        idx = 0
        while idx < len(pathToStart) and idx < len(pathToDest) and pathToStart[idx] == pathToDest[idx]:
            idx += 1
        
        pathToStart = (len(pathToStart) - idx) * 'U'
        pathToDest = ''.join(pathToDest[idx:])
        
        return pathToStart + pathToDest