class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = re.match("[+-]?[0-9]+", str.strip())
        if not r:
            return 0
        y = int(r.group())
        if y < -2147483648:
            y = -2147483648 
        if y > 2147483647:
            y = 2147483647
        return y
