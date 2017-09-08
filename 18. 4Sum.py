import itertools
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp = []
        for subset in itertools.combinations(nums, 4):
            if sum(list(subset)) == target:
                if sorted(list(subset)) not in temp:
                    temp.append(sorted(list(subset)))
        return temp