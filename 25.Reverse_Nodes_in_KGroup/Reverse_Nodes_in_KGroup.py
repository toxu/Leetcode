# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        count = 0
        while head:
            count += 1
            if count % k == 0:
                pre = self.reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        return dummy.next

    def reverse(self, pre, end):
        last = pre.next
        cur = last.next
        while cur != end:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last
