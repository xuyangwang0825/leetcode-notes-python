class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) :
        if not preorder:
            return None
        root = TreeNode(preorder[0])  # 创建根节点
        stack = [root]  # 栈，存储创建的节点
        index = 0  # 中序遍历数组中遍历索引
        for i in range(1, len(preorder)):  # 遍历前序数组，从第二个元素开始
            pre_order_node = TreeNode(preorder[i])
            if inorder[index] != stack[-1].val:  # 中序中索引指定的元素不等于栈顶元素
                node = stack[-1]
                node.left = pre_order_node  # 将前序遍历的当前结点添加为前一个节点的左子节点
                stack.append(node.left)
            else:  # 中序中索引指定的元素不等于栈顶元素
                while stack and inorder[index] == stack[-1].val:  # 找出栈中最后一个和中序遍历数组中相等的数
                    pop_node = stack.pop()  # 弹出相等的数
                    index += 1
                pop_node.right = pre_order_node  # 将前序遍历的当前节点添加为最后一个相等数的右子节点
                stack.append(pop_node.right)
        return root

sol = Solution()
pre = [3,9,20,15,7]
ino = [9,3,15,20,7]
tree = sol.buildTree(pre,ino)
print(tree)