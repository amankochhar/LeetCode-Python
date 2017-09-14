class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set(nums)) if len(nums) >= 1 else []