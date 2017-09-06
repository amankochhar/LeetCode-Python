class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return int(str(abs(x))[::-1]) == abs(x) if x>=0 else False