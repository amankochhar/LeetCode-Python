# will not work on LeetCode and give a Time Limit Exceeded error, but I really like the solution :)
import itertools
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ls = []
        for subset in itertools.combinations(nums, 3):
            if sum(list(subset))==0:
                if list(subset) not in ls:
                    ls.append(list(subset))
        return ls