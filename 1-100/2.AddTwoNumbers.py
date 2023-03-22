# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        cur1 = l1
        cur2 = l2
        
        carry = 0

        while cur2 or carry > 0:

            cur1.val += carry + (cur2.val if cur2 else 0)
            print(cur1.val)

            carry, cur1.val = cur1.val//10, cur1.val % 10
            print(cur1.val)

            if not cur1.next and ((cur2 and cur2.next) or carry > 0):
                cur1.next = ListNode(0)

            cur1 = cur1.next
            cur2 = cur2.next if cur2 else None


        
        return l1
