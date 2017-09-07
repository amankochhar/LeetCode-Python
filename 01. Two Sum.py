class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targ = target
        for index, i in enumerate(nums):
            targ -= i
            if targ in nums[index+1:]:
                return [index, nums[index+1:].index(targ)+index+1]
            else:
                targ = target
