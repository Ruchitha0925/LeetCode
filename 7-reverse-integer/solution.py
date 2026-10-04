// 18 ms | 12.3 MB
class Solution(object):
    def reverse(self, x):
        is_neg=x<0
        num=abs(x)
        rev=0
        while(num>0):
            rem=num%10
            if((rev*10+rem)>((2**31)-1) or (rev*10+rem)<(-(2**31))):
                return 0
                break
            rev=rev*10+rem
            num=num//10
        if(is_neg):
            return -rev
        return rev
        