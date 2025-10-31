class Solution(object):
    def productExceptSelf(self,nums):
        n=len(nums)
        result=[]
        
        for i in range(n):
            product=1
            for j in range(n):
                if j!=i:
                    product*=nums[j]
            result.append(product)
        return result
sol=Solution()
nums=[1,2,3,4]
print(sol.productExceptSelf(nums))
"""class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        result=[1]*n
        prefix=1
        for i in range(n):
            result[i]=prefix  #it will stores [1,1,2,6]
            prefix*=nums[i] #1*1=1 and goes on increasing of num[i]
        suffix=1
        for i in range(n-1,-1,-1):
            result[i]*=suffix #6*1=6
            suffix*=nums[i] #1*4=4 and goes on decreasing of num[i]
        return result
sol=Solution()
nums=[1,2,3,4]
print(sol.productExceptSelf(nums))
nums=[-1,1,0,-3,-3]
print(sol.productExceptSelf(nums))"""