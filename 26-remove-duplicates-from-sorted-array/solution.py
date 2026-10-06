// 0 ms | 13.1 MB
class Solution(object):
    def removeDuplicates(self, nums):
        num=sorted(list(set(nums)))
        for i in range(len(num)):
            nums[i]=num[i]
        return len(num)