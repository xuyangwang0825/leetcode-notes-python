class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isB(root: TreeNode):
            if not root.left == None and root.right == None :
                root.val = 1
            l, r = isB(root.left), isB(root.right)
            if l - r not in (0,-1,1): return False
            root. val = max(1+l,1+r)
        isB(root)
        return True

sol = Solution()
print(sol.myPow(2.00000,10))
print(sol.myPow2(2.00000,10))
