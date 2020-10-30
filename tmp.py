class Solution:
    def cuttingRope(self, n: int) -> int:
        i = n // 3
        j = n % 3
        res = max(pow(3,i),pow(2,k)
        return res * j if i != 0 else 1

sol = Solution()
print(sol.cuttingRope(10))
