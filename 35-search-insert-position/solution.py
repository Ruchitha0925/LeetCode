// 0 ms | 12.9 MB
class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            if(target<nums[mid]):
                r=mid-1
            elif(target>nums[mid]):
                l=mid+1
            else:
                return mid
        return l