class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies=max(candies)
        result=[]
        for i in range (len(candies)):
            sol=candies[i]+extraCandies>=maxCandies
            result.append(sol)
        return result
sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies))