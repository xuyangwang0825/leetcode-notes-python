### [xxxx.lalala](https://leetcode-cn.com/problems/miao/)

#### 问题描述


**Example:**
```python

```

#### 思路

#### 代码

```python

```

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre,cur = head,head.next
        while cur and cur.val != val:
            pre,cur = cur,cur.next
        if cur: pre.next = cur.next
        return head