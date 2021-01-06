### [32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

#### 问题描述
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

**Example:**
```python
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
```

#### 思路
- 设一个flag，每一层反向存储
#### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        quene = [root]
        res = []
        level = 0
        flag = False
        while quene:
            res.append([])
            for _ in range(len(quene)):
                tmp = quene.pop(0)
                if not flag:
                    res[level].append(tmp.val)
                else:
                    res[level] = [tmp.val] + res[level]
                if tmp.left: quene.append(tmp.left) 
                if tmp.right: quene.append(tmp.right) 
            flag = False if flag else True
            level += 1
        return res
```