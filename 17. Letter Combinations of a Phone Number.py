import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyLetter = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        availLetters = []
        for digit in list(digits):
            availLetters.append(list(keyLetter[int(digit)]))
        ans = ([''.join(s) for s in itertools.product(*availLetters)])
        return ans if len(ans) > 1 else []