# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        nodes = []
        odd_flag = True
        dummy = TreeNode(-1)
        current = dummy
        while head:
            if odd_flag:
                current.next = head
                odd_flag = False
                head = head.next
                current = current.next
                current.next = None
            else:
                nodes.append(head)
                odd_flag = True
                head = head.next
        while nodes:
            tmp = nodes.pop(0)
            current.next = tmp
            current = current.next
            current.next = None
        return dummy.next
