class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        correct = {"]":"[", "}":"{", ")":"("}
        for bracket in s:
            if bracket in correct.values():
                stack.append(bracket)
            elif bracket in correct.keys():
                if stack == [] or correct[bracket] != stack.pop():
                    return False
            else:
                return False
        return stack == []