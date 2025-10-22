class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        length = gcd(len(str1),len(str2))
        return str1[:length]
sol=Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB")) 
print(sol.gcdOfStrings("LEET", "CODE"))