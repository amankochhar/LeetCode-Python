class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = nums1 + nums2
        temp.sort()
        index = len(temp)/2
        print(temp, index)
        if len(temp) == 2:
            return (temp[0] + temp[1])/2.0
        if len(temp)%2 == 0:
            return (temp[index-1] + temp[index])/2.0
        else:
            return temp[index]