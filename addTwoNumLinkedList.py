# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        out = ListNode(0)
        current = out
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carry
            carry = 0
            if sum >= 10:
                carry = sum//10
                sum = sum % 10
            current.next = ListNode(sum)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry: current.next = ListNode(carry)
        return out.next



        
