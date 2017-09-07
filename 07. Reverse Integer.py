class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = int(str(abs(x))[::-1])
        answer = answer * -1 if x < 0 else answer
        return answer if -2147483648 <= answer <= 2147483647 else 0
