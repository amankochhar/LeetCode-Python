class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for i in zip(*strs):
            if len(set(i)) > 1: break
            ans += i[0]
            
        return ans

        # second solution
        #import os
        #return os.path.commonprefix(strs)