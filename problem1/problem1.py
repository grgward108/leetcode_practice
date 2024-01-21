class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i, num  in enumerate(nums):
            hash[num] = i


        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash and hash[complement] != i:
                return [i, hash[complement]]


        return []

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """