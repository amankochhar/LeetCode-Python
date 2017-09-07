# there are two solutions for this questions. You can't use them on LeetCode TLE but these are good to remeber for whiteboarding
# and for knowledge
'''
1. uses itertools and min to figure out which sum is the closest to target
'''
import itertools
class Solution(object):
    def threeSumClosestIter(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        temp = set()
        for subset in itertools.combinations(nums, 3):
            temp.add(sum(list(subset)))
        return min(temp, key=lambda x:abs(x-target))
        
'''
2. Uses bisect_left which works similar to binary search and is much faster IF THE LIST IS SORTED - O(n logn)
'''
from bisect import bisect_left
class Solution(object):
    def threeSumClosestBisect(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def takeClosest(self, myList, myNumber):
            """
            Assumes myList is sorted. Returns closest value to myNumber.
            If two numbers are equally close, return the smallest number.
            """
            pos = bisect_left(myList, myNumber)
            if pos == 0:
                return myList[0]
            if pos == len(myList):
                return myList[-1]
            before = myList[pos - 1]
            after = myList[pos]
            if after - myNumber < myNumber - before:
                return after
            else:
                return before

        temp = set()
        for subset in itertools.combinations(nums, 3):
            temp.add(sum(list(subset)))
        temp = sorted(temp) # should be a sorted array by default for bisect_left to work in O(n logn)
        return takeClosest(self, temp, target)