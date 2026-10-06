// 3 ms | 13.2 MB
class Solution(object):
    def removeDuplicates(self, nums):
        num=sorted(list(set(nums)))
        for i in range(len(num)):
            nums[i]=num[i]
            l=len(num)
        return l