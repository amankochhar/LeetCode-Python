class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #O(NM) time, O(NM) space
        lenS, lenP = len(s), len(p)
        dp = [[False for j in xrange(lenP + 1)] for i in xrange(lenS + 1)]
        
        #Base cases - empty string matches w/ empty pattern
        dp[0][0] = True
        
        #empty string to nonempty pattern
        for i in xrange(1, lenP + 1):
            if i > 1 and p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
                    
        #DP cases
        for i in xrange(1, lenS + 1):
            for j in xrange(1, lenP + 1):
                #If the string char equals the pattern char or the pattern is a dot,  
                #there is a dp if everything before matches
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                #Star can only dp if there is something before the star to dp
                elif j > 1 and p[j - 1] == '*':
                    #If the character before the star matches char in the string,
                    #the star can dp 0 of the char before it, or at least 1.
                    #dp[i][j-2] is for matching 0, cause we need to skip the last 2
                    #characters in the pattern. dp[i - 1][j] is for matching 1, cause
                    #we need to skip 1 character in the string, but keep the entire pattern
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    #If the character before the star does not dp the char in the string,
                    #then the only way to get a dp is if the star matches 0 characters
                    else:
                        dp[i][j] = dp[i][j - 2]
                        
        return dp[lenm][lenP]