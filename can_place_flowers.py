"""class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
      while flowerbed[n]==1:
        return True
      while flowerbed[n]==0:
        return False
sol=Solution()
flowerbed=[1,0,0,0,1]
n=0
print(sol.canPlaceFlowers(flowerbed,n))
n=1
print(sol.canPlaceFlowers(flowerbed,n))"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                empty_left=(i==0) or (flowerbed[i-1]==0)
                empty_right=(i==len(flowerbed)) or (flowerbed[i+1]==0)
                if empty_left and empty_right:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                     return True
        return n<=0
sol=Solution()
flowerbed=[1,0,0,0,1]
n=1
print(sol.canPlaceFlowers(flowerbed,n))
n=2
print(sol.canPlaceFlowers(flowerbed,n))