# Leetcode刷题之路

> ## **2020.1.11**

1     [Two Sum](https://leetcode-cn.com/problems/two-sum/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1 = 0
        start = ListNode(0)
        l1_literal = 0
        l2_literal = 0
        flag = 0
        while not l1 == None:
            l1_literal += l1.val * 10 ** i1
            l1 = l1.next
            i1 += 1
        i2 = 0
        while not l2 == None:
            l2_literal += l2.val * 10 ** i2 
            l2 = l2.next
            i2 += 1
        result = str(l1_literal + l2_literal)
        for i in range(len(result)-1,-1,-1):
            if flag == 0:
                tmp = ListNode(int(result[i]))
                start = tmp
                tmp1 = tmp
                flag = 1
            else:
                tmp2 = ListNode(int(result[i]))
                tmp1.next = tmp2
                tmp1 = tmp1.next
        return start
```

  2.   [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hdict = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if nums[i] in hdict:
                return hdict[nums[i]],i
            else:
                hdict[remain] = i
```

> ## **2020.1.12**