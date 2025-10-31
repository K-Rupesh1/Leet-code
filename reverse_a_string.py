class Solution(object):
    def reverseString(self,s):
        words=s.split() # split method is used for to convert string into a list 
        words.reverse()
        return " ".join(words)
sol=Solution()
s="the sky is blue"
print(sol.reverseString(s))
s="hello   world"
print(sol.reverseString(s))