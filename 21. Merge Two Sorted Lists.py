# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = res = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res, l1 = res.next, l1.next
            else:
                res.next = l2
                res, l2 = res.next, l2.next
        res.next = l1 or l2
        return ans.next