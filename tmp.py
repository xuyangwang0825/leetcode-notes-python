class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n % 2
            n //= 2
        res += 1
        return res

sol = Solution()
print(sol.hammingWeight(11))
