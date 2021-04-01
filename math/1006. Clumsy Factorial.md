### [1006. Clumsy Factorial](https://leetcode-cn.com/problems/clumsy-factorial/)

#### 问题描述
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

**Example:**
```python
Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
```
```python
Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
```

#### 思路
- 一次遍历（模拟）
- 数学推导（找规律）

#### 代码

```python
class Solution:
    def clumsy(self, N: int) -> int:
        tmp = 0
        res = 0
        for i,num in enumerate(range(N,0,-1)):
            if i % 4 == 0:
                tmp = num if i == 0 else -num
            elif i % 4 == 1:
                tmp *= num
            elif i % 4 == 2:
                if tmp < 0: res -= -tmp // num
                else:
                    res += tmp // num
                tmp = 0
            else:
                res += num
        if tmp != 0:
            res += tmp
        return res
```
```python
class Solution:
    def clumsy(self, N: int) -> int:
        return N + ((3, 0, 0, 3) if N <= 4 else (1, 2, 2, -1))[N % 4]
```