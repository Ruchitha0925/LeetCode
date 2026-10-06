// 0 ms | 12.2 MB
class Solution(object):
    def removeElement(self, nums, val):
        num=[x for x in nums if x!=val]
        for i in range(len(num)):
            nums[i]=num[i]
        return len(num)