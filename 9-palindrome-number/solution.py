// 21 ms | 12.3 MB
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        num=abs(x)
        rev=0
        while(num>0):
            rem=num%10
            rev=rev*10+rem
            num=num//10
        if rev==x:
            return True
        else:
            return False