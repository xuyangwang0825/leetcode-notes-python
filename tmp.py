class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i,j = 0,0
        while j < len(p):
            pre = p[j]
            if j+1 < len(p): cur = p[j+1]
            if j != len(p)-1 and cur == '*':
                while i < len(s) and (s[i] == pre or pre == '.'): i += 1
                if i == len(s): return False
                j += 2
            else:
                if pre not in ('.','*'):
                    if s[i] and pre == s[i]:
                        i,j = i+1,j+1
                    else: return False
                elif pre == '.':
                    if s[i]:
                        i,j = i+1,j+1
                    else: return False
        if i == len(s): return True
        else:return False


sol = Solution()
print(sol.isMatch("ab",".*c"))
