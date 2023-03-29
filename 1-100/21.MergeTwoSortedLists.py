# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val < list2.val:
            cur1, cur2 = list1, list2
        else:
            cur1, cur2 = list2, list1

        while cur2:
            if (not cur1.next) or cur2.val < cur1.next.val:
                cur1.next, cur2.next, cur2 = cur2, cur1.next, cur2.next

            cur1 = cur1.next

            if not cur1.next:
                cur1.next = cur2
                break

            

        if list1.val < list2.val:
            return list1
        return list2
                
                

        # output = ListNode(0)
        # cur3 = output
        # while cur1 and cur2:
        #     if cur1.val < cur2.val:
        #         cur3.next = ListNode(cur1.val)
        #         cur3 = cur3.next
        #         cur1 = cur1.next
        #     else:
        #         cur3.next = ListNode(cur2.val)
        #         cur3 = cur3.next
        #         cur2 = cur2.next
        
        # while cur1:
        #     cur3.next = ListNode(cur1.val)
        #     cur3 = cur3.next
        #     cur1 = cur1.next

        # while cur2:
        #     cur3.next = ListNode(cur2.val)
        #     cur3 = cur3.next
        #     cur2 = cur2.next

        # return output.next
        
