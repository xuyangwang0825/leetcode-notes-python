class Solution:
    visited = set()
    m,n,k =0,0,0
    def dfs(self,i,j,si,sj):
        if i >= self.m or j >= self.n or self.k < si + sj or (i,j) in self.visited: return 0
        self.visited.add((i,j))
        return 1 + self.dfs(i+1,j,si+1 if (i+1) % 10 else si-8,sj) + self.dfs(i,j+1,si,sj+1 if (j+1) % 10 else sj-8)
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.m,self.n,self.k = m,n,k
        return self.dfs(0,0,0,0)

sol = Solution()
print(sol.movingCount(3,2,17))
