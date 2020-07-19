# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):
        if not root:
            return
            #如只有左子树或左右子树时每一层二维数组由左子树建立
        if len(res) == level:
            #建立存储每一层二维数组
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1, res)
        if root.right:
            self.dfs(root.right, level + 1, res)