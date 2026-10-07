// 15 ms | 15.2 MB
class Solution(object):
    def singleNumber(self, nums):
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for key,val in dict.items():
            if val==1:
                return key
