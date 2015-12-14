# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            v = l1.val + l2.val + flag
            flag, num = v/10, v%10
            current.next = ListNode(num)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        if l1 and not l2:
            while l1:
                v = l1.val + flag
                flag, num = v/10, v%10
                current.next = ListNode(num)
                current = current.next
                l1 = l1.next
        elif not l1 and l2:
            while l2:
                v = l2.val + flag
                flag, num = v/10, v%10
                current.next = ListNode(num)
                current = current.next
                l2 = l2.next
        if flag == 1:
            current.next = ListNode(1)
            current = current.next
        current.next = None
        return dummy.next