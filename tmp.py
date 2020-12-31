
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return None
            if root.right:
                tmp = dfs(root.right)
                if tmp: return tmp

            if self.k: self.k -= 1
            if not self.k: return root.val

            if root.left:
                tmp = dfs(root.left)
                if tmp: return tmp
        self.k = k
        return dfs(root)



sol = Solution()
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right = TreeNode(4)
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
print(sol.kthLargest(root,3))
