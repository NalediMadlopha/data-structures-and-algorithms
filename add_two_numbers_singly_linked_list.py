# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        p1 = l1
        p2 = l2

        while p1 is not None or p2 is not None:
            x = p1.val if p1 is not None else 0
            y = p2.val if p2 is not None else 0
            sum = x + y + carry

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            if p1 is not None:
                p1 = p1.next

            if p2 is not None:
                p2 = p2.next

        if carry > 0:
            current.next = ListNode(1)

        return dummy_head.next