class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowerbed = flowerbed + [0]
        i,length = 0,len(flowerbed)-1

        while i < length:
            if flowerbed[i]:
                i += 2
            elif flowerbed[i+1]:
                i += 3
            else:
                n -= 1
                i += 2

        return n <= 0



sol = Solution()
print(sol.canPlaceFlowers([0,1,1,0,0],1))
