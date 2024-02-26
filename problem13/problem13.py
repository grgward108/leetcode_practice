class Solution(object):
    def findPeakElement(self, nums):

        l, r = 0, len(nums)-1 
        while l < r:
            middle = (l+r)//2
            if nums[middle] > nums[middle + 1]:
                r = middle
            else:
                l = middle + 1

        return l