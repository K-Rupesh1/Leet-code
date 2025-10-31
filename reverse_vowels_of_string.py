class Solution(object):
    def reverseVowels(self,input):
        input=list(input)
        n=len(input)
        left=0
        right=n-1
        vowels=set("aeiouAEIOU")
        while left < right:
            while left < right and input[left]  not in vowels:
                left+=1
            while left < right and input[right] not in vowels:
                right-=1
            input[left],input[right]=input[right],input[left]
            left+=1
            right+=1 
        input="".join(input)
        return input


sol=Solution()
input="IcecreAm"
print(sol.reverseVowels(input))