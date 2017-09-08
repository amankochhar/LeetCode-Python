# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        n1, n2 = head, head
        for _ in range(n):
            n2 = n2.next
        if n2 == None:
            head, n1.next = n1.next, None
            return head
        while n2.next:
            n1, n2 = n1.next, n2.next
        temp = n1.next
        n1.next = temp.next
        temp.next = None
        return head