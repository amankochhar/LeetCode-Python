class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, l, r, ans=[]):
            if l:         
                generate(p + '(', l-1, r)
            if r > l: 
                generate(p + ')', l, r-1)
            if not r:    
                ans += p,
            return ans
        return generate('', n, n)