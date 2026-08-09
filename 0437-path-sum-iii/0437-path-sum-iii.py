# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

        
        def dfs(node,total):
            if node is None:
                return 0
            total+=node.val

            count=0

            if total==targetSum:
                count=1
            count+=dfs(node.left,total)
            count+=dfs(node.right,total)

            return count
        if root is None:
            return 0

            #start next node change node

        return (
            dfs(root,0)
            +self.pathSum(root.left,targetSum)
            +self.pathSum(root.right,targetSum)
        )