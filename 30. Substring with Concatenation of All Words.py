import itertools
import re

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # this method won't work for a very long list of words
        combos = list(set(map(lambda x: "".join(x), list(itertools.permutations(words, len(words))))))
        return [n for combo in combos for n in range(len(s)) if s.find(combo, n) == n]
        #return list(set([match.start() for combo in combos for match in re.finditer(combo,s)])) # will NOT find overlapping sewuences
