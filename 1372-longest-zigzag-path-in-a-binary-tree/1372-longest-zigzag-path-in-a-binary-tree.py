# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans=0

        def dfs(root,dir,len):
            nonlocal ans

            if root is None:
                return
            ans=max(ans,len)

            if dir=="left":
                dfs(root.right,"right",len+1)
                dfs(root.left,"left",1)
            else:
                dfs(root.left,"left",len+1)
                dfs(root.right,"right",1)
        dfs(root.left,"left",1)
        dfs(root.right,"right",1)

        return ans


        