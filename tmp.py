class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0: return res
        if n < 0: x, n = 1/x, -n
        while n:
            if n % 2: res *= x
            x *= x
            n //= 2
        return res
    def myPow2(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

sol = Solution()
print(sol.myPow(2.00000,10))
print(sol.myPow2(2.00000,10))
