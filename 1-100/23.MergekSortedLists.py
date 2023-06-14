# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(head_1, head_2):
    output = ListNode()
    cur = output

    while head_1 and head_2:
        if head_1.val < head_2.val:
            cur.next = head_1
            head_1 = head_1.next
        else:
            cur.next = head_2
            head_2 = head_2.next
        cur = cur.next

    if head_1:
        cur.next = head_1
    else:
        cur.next = head_2

    return output.next

def halve(lists):
    output = []

    for i in range(0, len(lists) - 1, 2):
        output.append(merge(lists[i], lists[i + 1]))

    if len(lists) % 2 == 1:
        output.append(lists[-1])

    return output

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
            
        while len(lists) > 1:
            lists = halve(lists)

        return lists[0]
        
