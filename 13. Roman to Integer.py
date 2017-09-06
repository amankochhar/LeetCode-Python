class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        # using the lists from problem 12
        romans = dict((n,v) for n,v in zip(numerals, values))

        prev = total =0
        
        for i in range(len(s)-1, -1, -1):
            val = romans[s[i]]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        
        return total